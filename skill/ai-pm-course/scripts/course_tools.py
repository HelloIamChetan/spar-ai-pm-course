#!/usr/bin/env python3
"""
course_tools.py — helpers for the ai-pm-course local-markdown backend.

    python course_tools.py status  --tracker tracker.md --ledger ledger.md
    python course_tools.py next    --tracker tracker.md
    python course_tools.py verify  --tracker tracker.md --ledger ledger.md --chapter 4
    python course_tools.py delta   --bank bank.md --ledger ledger.md [--threshold 0.85]

Reads the markdown tables described in assets/templates/. Never writes anything.
Stdlib only.
"""

import argparse
import difflib
import re
import signal
import sys
from pathlib import Path

# Let `... | head` close the pipe without dumping a traceback at the user.
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

GLYPHS = ["⬜", "📖", "✅", "🆕", "⛔"]


# ---------- markdown parsing ----------

def read(path):
    return Path(path).read_text(encoding="utf-8")


def sections(md):
    """Split on '## ' headings → {heading: body}. Text before the first heading is under ''."""
    out, current, buf = {}, "", []
    for line in md.splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            out[current] = "\n".join(buf)
            current, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    out[current] = "\n".join(buf)
    return out


def tables(md):
    """Return every markdown table in md as (headers, rows) with cells stripped."""
    found, block = [], []
    for line in md.splitlines() + [""]:
        if line.strip().startswith("|"):
            block.append(line)
        else:
            if len(block) >= 2:
                cells = [[c.strip() for c in row.strip().strip("|").split("|")] for row in block]
                headers = cells[0]
                rows = [r for r in cells[2:] if any(r)] if re.match(r"^\s*\|?\s*:?-+", block[1]) else cells[1:]
                found.append((headers, rows))
            block = []
    return found


def table_with(md, *needles):
    """First table whose header row contains every needle (case-insensitive)."""
    for headers, rows in tables(md):
        h = " ".join(headers).lower()
        if all(n.lower() in h for n in needles):
            return headers, rows
    return None, []


def col(headers, *names):
    for i, h in enumerate(headers):
        if any(n.lower() == h.lower() or n.lower() in h.lower() for n in names):
            return i
    return None


def glyph_of(status):
    for g in GLYPHS:
        if status.startswith(g):
            return g
    return "?"


# ---------- loaders ----------

def load_curriculum(tracker_md):
    headers, rows = table_with(tracker_md, "chapter", "status")
    if headers is None:
        sys.exit("tracker: no curriculum table (needs 'Chapter' and 'Status' columns)")
    ci, ni, qi, si = col(headers, "#", "num"), col(headers, "chapter"), col(headers, "question"), col(headers, "status")
    out = []
    for r in rows:
        try:
            num = int(re.sub(r"\D", "", r[ci])) if ci is not None else len(out) + 1
        except ValueError:
            continue
        out.append({"n": num, "title": r[ni], "questions": r[qi] if qi is not None else "", "status": r[si] if si is not None and si < len(r) else ""})
    return out


def load_ledger(ledger_md):
    headers, rows = table_with(ledger_md, "q", "status")
    if headers is None:
        sys.exit("ledger: no ledger table (needs a Q-id column and a Status column)")
    qi, ti, hi, si = col(headers, "q-id", "qid", "id"), col(headers, "question"), col(headers, "home", "ch"), col(headers, "status")
    di, sci = col(headers, "drilled"), col(headers, "score")
    out = []
    for r in rows:
        if qi is None or qi >= len(r) or not r[qi]:
            continue
        get = lambda i: r[i] if i is not None and i < len(r) else ""
        out.append({"qid": get(qi), "question": get(ti), "home": get(hi), "status": get(si), "drilled": get(di), "score": get(sci)})
    return out


def load_cycle_log(tracker_md):
    body = sections(tracker_md).get("Cycle log", "")
    headers, rows = (tables(body) or [(None, [])])[0]
    return headers, rows


# Bank sections that hold prose, not questions. Bullets under these headings are ignored.
META_SECTIONS = re.compile(r"^(sources?|credits?|attribution|notes?|changelog|how to use|usage|license|licence|contents?|index)\b", re.I)


def load_bank_questions(bank_md):
    """Bullet lines from a bank file, minus the parts that aren't questions.

    Skipped: bullets under a meta heading (Sources, Credits, Notes, ...), bullets in the
    preamble before the first '##' heading when the file uses headings at all, blockquote
    lines, and appended model-answer blocks. Without this, a delta check reports the
    bank's own source list as a pile of brand-new questions.
    """
    has_headings = bool(re.search(r"^##\s+", bank_md, re.M))
    qs, heading, seen_heading = [], "", False
    for line in bank_md.splitlines():
        h = re.match(r"^#{2,6}\s+(.*\S)\s*$", line)
        if h:
            heading, seen_heading = h.group(1).strip(), True
            continue
        if has_headings and (not seen_heading or META_SECTIONS.match(heading)):
            continue
        m = re.match(r"^\s*(?:[-*•]|\d+[.)])\s+(.*\S)\s*$", line)
        if m and not line.strip().startswith(">"):
            text = m.group(1)
            if text.startswith("✔") or text.lower().startswith("model answer"):
                continue
            qs.append(text)
    return qs


def normalize(s):
    s = s.lower()
    s = re.sub(r"[`*_~]", "", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


STOP = set("a an the and or of to in on for is are it its be do does how what when why would you your we our this that with at by from as vs".split())


def stem(w):
    for suf in ("ations", "ation", "ings", "ing", "ers", "er", "ies", "es", "s", "ed", "al"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def content_words(n):
    return {stem(w) for w in n.split() if w not in STOP and len(w) > 2}


def similarity(a, b):
    """Max of character-level ratio and stemmed content-word Jaccard — the second catches rephrases."""
    r = difflib.SequenceMatcher(None, a, b).ratio()
    wa, wb = content_words(a), content_words(b)
    j = len(wa & wb) / len(wa | wb) if wa and wb else 0.0
    return max(r, j)


# ---------- commands ----------

def cmd_status(a):
    tracker, ledger = read(a.tracker), read(a.ledger)
    cur, led = load_curriculum(tracker), load_ledger(ledger)
    by = {g: 0 for g in GLYPHS + ["?"]}
    for c in cur:
        by[glyph_of(c["status"])] += 1
    nxt = next((c for c in cur if not c["status"].startswith("✅")), None)
    lg = {g: 0 for g in GLYPHS + ["?"]}
    for q in led:
        lg[glyph_of(q["status"])] += 1
    print(f"Chapters: {len(cur)} total · ✅ {by['✅']} · 📖 {by['📖']} · ⬜ {by['⬜']}")
    print(f"Ledger:   {len(led)} questions · ✅ {lg['✅']} · 📖 {lg['📖']} · ⬜ {lg['⬜']} · 🆕 {lg['🆕']} · ⛔ {lg['⛔']}")
    print(f"Next:     Ch {nxt['n']} — {nxt['title']}" if nxt else "Next:     all chapters ✅")
    sess_h, sess_r = table_with(tracker, "session", "status")
    if sess_h is not None:
        si = col(sess_h, "status")
        done = sum(1 for r in sess_r if si is not None and si < len(r) and r[si].startswith("✅"))
        print(f"Sessions: {len(sess_r)} optional · ✅ {done}")
    dq = sections(tracker).get("Delta queue", "")
    _, dq_rows = (tables(dq) or [(None, [])])[0]
    print(f"Delta queue: {len(dq_rows)}")
    headers, rows = load_cycle_log(tracker)
    if rows:
        print("Last cycles:")
        for r in rows[-3:]:
            print("  " + " · ".join(r))
    else:
        print("Last cycles: none logged")


def cmd_next(a):
    cur = load_curriculum(read(a.tracker))
    nxt = next((c for c in cur if not c["status"].startswith("✅")), None)
    print(f"{nxt['n']}\t{nxt['title']}" if nxt else "done")


def norm_home(cell):
    """'Ch4' / 'ch 4' / '4' -> 'CH4'; 'S25' -> 'S25'; anything else uppercased and squeezed."""
    c = re.sub(r"\s+", "", (cell or "")).upper()
    if re.fullmatch(r"\d+", c):
        return "CH" + c
    return c


def cmd_verify(a):
    tracker, ledger = read(a.tracker), read(a.ledger)
    cur, led = load_curriculum(tracker), load_ledger(ledger)
    want = norm_home(a.chapter)
    num = int(re.sub(r"\D", "", want) or 0)
    is_session = want.startswith("S")
    row = None if is_session else next((c for c in cur if c["n"] == num), None)
    label = want.replace("CH", "Ch ")
    print(f"Tracker row: {label} — {row['title']} → {row['status'] or '(empty)'}" if row
          else f"Tracker row: {label} " + ("is an optional session — check the sessions table by hand" if is_session else "NOT FOUND"))
    mine = [q for q in led if norm_home(q["home"]) == want]
    print(f"Ledger rows for {label}: {len(mine)}")
    for q in mine:
        extra = f" · {q['drilled']} · {q['score']}" if q["drilled"] or q["score"] else ""
        print(f"  {q['qid']} {q['status'] or '(empty)'}{extra} — {q['question'][:70]}")
    headers, rows = load_cycle_log(tracker)
    if rows:
        last = rows[-1]
        if headers:
            pairs = [f"{h}: {c}" for h, c in zip(headers, last) if c]
            print("Last log line: " + " · ".join(pairs))
        else:
            print("Last log line: " + " · ".join(last))
    else:
        print("Last log line: none")


def cmd_delta(a):
    bank, ledger = read(a.bank), read(a.ledger)
    bq, led = load_bank_questions(bank), load_ledger(ledger)
    ln = [(normalize(q["question"]), q) for q in led]
    new, matched_ledger = [], set()
    for q in bq:
        nq = normalize(q)
        best, best_r = None, 0.0
        for n, row in ln:
            r = 1.0 if n == nq else similarity(n, nq)
            if r > best_r:
                best, best_r = row, r
        if best and best_r >= a.threshold:
            matched_ledger.add(best["qid"])
            if best_r < 1.0:
                print(f"~ near-match ({best_r:.2f}) {best['qid']}: {q[:80]}")
        else:
            new.append((q, best, best_r))
    print(f"\nBank questions not in ledger: {len(new)}")
    for q, best, r in new:
        hint = f"  (closest: {best['qid']} @ {r:.2f})" if best else ""
        print(f"  + {q}{hint}")
    gone = [q for q in led if q["qid"] not in matched_ledger]
    print(f"\nLedger rows with no bank match: {len(gone)}")
    for q in gone:
        print(f"  - {q['qid']} {q['status']} {q['question'][:80]}")
    print("\nTriage each '+' line: rephrase → propose merge (OK before editing the bank); new + covered topic → Delta queue; new + future topic → 🆕 in ledger; out of scope → ⛔.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("status"); s.add_argument("--tracker", required=True); s.add_argument("--ledger", required=True); s.set_defaults(f=cmd_status)
    s = sub.add_parser("next"); s.add_argument("--tracker", required=True); s.set_defaults(f=cmd_next)
    s = sub.add_parser("verify"); s.add_argument("--tracker", required=True); s.add_argument("--ledger", required=True); s.add_argument("--chapter", required=True, help="chapter number, 'Ch4', or a session code like S25"); s.set_defaults(f=cmd_verify)
    s = sub.add_parser("delta"); s.add_argument("--bank", required=True); s.add_argument("--ledger", required=True); s.add_argument("--threshold", type=float, default=0.85); s.set_defaults(f=cmd_delta)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
