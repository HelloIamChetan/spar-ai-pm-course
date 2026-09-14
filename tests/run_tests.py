#!/usr/bin/env python3
"""Test suite. Stdlib only, no network, runs in seconds.

The tests are chosen around what this repo promises and what would quietly break it:

  - The bank and the ledger must stay byte-identical in question text. The delta check
    matches ledger rows to bank questions by text, so drift there makes every future check
    re-flag questions that are already indexed. `build_course.py --check` owns that.
  - Every question must credit a declared source, and the sources' own answer guidance and
    named frameworks must stay out. That is the licence promise in LICENSE-CONTENT, and a
    promise nothing checks is a promise waiting to be broken.
  - The skill must stay stdlib-only with no network calls and no external storage. "Your
    data is four markdown files you own" stops being true the moment someone adds `requests`.

    python3 tests/run_tests.py
"""

import ast
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skill" / "ai-pm-course"
COURSE = ROOT / "course"

FAILURES, CHECKS = [], 0


def check(name, ok, detail=""):
    global CHECKS
    CHECKS += 1
    if ok:
        print(f"  pass  {name}")
    else:
        print(f"  FAIL  {name}" + (f"\n        {detail}" if detail else ""))
        FAILURES.append(name)


def bank_questions(text):
    """Question bullets, source tag stripped. Section headers start with '**' and are skipped."""
    return [re.sub(r"— \*[^*]+\*\s*$", "", q).strip()
            for q in re.findall(r"^- (.+)$", text, re.M) if not q.startswith("**")]


def ledger_rows(text):
    """Every ledger row, whatever the chapter column holds — Ch12, S25 and — are all valid."""
    return re.findall(r"^\| (Q\d+) \| (.+?) \| (.+?) \| (\S*)", text, re.M)


# ---------- 1. the generated files match their source ----------

def test_generated():
    print("\ngenerated files match their source")
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_course.py"), "--check"],
                       capture_output=True, text=True, cwd=ROOT)
    check("build_course.py --check passes (bank and ledger match QUESTIONS)",
          r.returncode == 0, (r.stdout + r.stderr).strip()[-400:])


# ---------- 2. bank and ledger agree ----------

def test_bank_ledger(bank, ledger, tracker):
    print("\nbank and ledger agree")
    bq, rows = bank_questions(bank), ledger_rows(ledger)
    lq = [r[1].strip() for r in rows]

    claimed = int(re.search(r"\*\*(\d+) questions\.\*\*", bank).group(1))
    check(f"bank's own claim of {claimed} matches the bullets it has",
          claimed == len(bq), f"claims {claimed}, has {len(bq)}")
    check("ledger has exactly one row per bank question",
          len(rows) == len(bq), f"{len(rows)} rows vs {len(bq)} questions")
    check("no duplicate questions in the bank",
          len(set(bq)) == len(bq), f"{len(bq) - len(set(bq))} duplicates")

    # The invariant the delta check depends on. Order matters as much as membership:
    # the ledger is in bank order and stays that way.
    drift = [(i + 1, b, l) for i, (b, l) in enumerate(zip(bq, lq)) if b != l]
    check("ledger question text is byte-identical to the bank, in bank order",
          not drift, "; ".join(f"Q{i:03d}: {b[:40]!r} vs {l[:40]!r}" for i, b, l in drift[:3]))

    ids = [r[0] for r in rows]
    check("Q-ids are sequential and unique", ids == [f"Q{i:03d}" for i in range(1, len(ids) + 1)],
          f"first mismatch near {next((a for a, b in zip(ids, [f'Q{i:03d}' for i in range(1, len(ids)+1)]) if a != b), '?')}")

    # Tracker's per-chapter counts are shown to the learner as progress denominators.
    tcounts = {int(a): int(b) for a, b in re.findall(r"^\| (\d+) \| .+? \| (\d+) \|", tracker, re.M)}
    actual = Counter(int(c[2:]) for _, _, c, _ in rows if c.startswith("Ch"))
    bad = {c: (tcounts[c], actual.get(c, 0)) for c in tcounts if tcounts[c] != actual.get(c, 0)}
    check("tracker's per-chapter question counts match the ledger", not bad,
          "; ".join(f"Ch{c}: says {a}, is {b}" for c, (a, b) in list(bad.items())[:4]))
    check("every ledger chapter exists in the tracker curriculum, or is a session/out-of-scope",
          all(c.startswith(("Ch", "S")) or c == "—" for _, _, c, _ in rows))


# ---------- 3. the licence promise ----------

# Named, branded frameworks belong to their authors. Questions may *name* one; what must never
# appear is the framework reproduced or explained. Any hit here is a manual review, not a crash.
BRANDED = re.compile(
    r"\b(CIRCLES|RICE scor|HEART framework|AARRR|pirate metric|Kano model|MoSCoW|ICE scor|"
    r"Hook Model|Working Backwards|STAR method|SPSIL|Lewis Lin|Exponent|Product Alliance|Reforge)\b", re.I)

# Answer-guidance shapes. A bank entry is a question; prose telling you what to say is not.
GUIDANCE = re.compile(r"\b(you should|the answer is|key point|remember to|the framework is|"
                      r"a strong answer|model answer)\b", re.I)


def test_licence_promise(bank):
    print("\nlicence promise: questions only, every one credited")
    declared = set(re.findall(r"^- \*\*([A-Z0-9-]+)\*\* —", bank, re.M))
    check("sources are declared in the bank", len(declared) >= 2, f"{sorted(declared)}")

    qs = [q for q in re.findall(r"^- (.+)$", bank, re.M) if not q.startswith("**")]
    used, orphans = set(), []
    for q in qs:
        m = re.search(r"— \*([^*]+)\*\s*$", q)
        if m:
            used |= {s.strip() for s in m.group(1).split(",")}
        else:
            orphans.append(q)
    check("every question credits at least one source", not orphans,
          "; ".join(o[:60] for o in orphans[:3]))
    check("every cited source is declared", not (used - declared), f"undeclared: {sorted(used - declared)}")
    check("every declared source is actually cited", not (declared - used), f"unused: {sorted(declared - used)}")

    branded = [q for q in bank_questions(bank) if BRANDED.search(q)]
    check("no branded framework reproduced in the bank", not branded,
          "; ".join(b[:60] for b in branded[:3]))
    guidance = [q for q in bank_questions(bank) if GUIDANCE.search(q)]
    check("no answer guidance in the bank — questions only", not guidance,
          "; ".join(g[:60] for g in guidance[:3]))
    check("bank states that guidance and frameworks are not reproduced",
          "not** reproduced here" in bank or "not reproduced" in bank)


# ---------- 4. no external dependencies ----------

# Stdlib modules this repo is allowed to use. The point is not to police the standard library
# but to make adding a third-party dependency a deliberate act that shows up in a diff — the
# "no database, no account, no subscription" promise lives or dies on this.
STDLIB_OK = {"argparse", "ast", "collections", "difflib", "json", "os", "pathlib", "re",
             "signal", "subprocess", "sys", "textwrap", "unicodedata", "datetime", "shutil",
             "zipfile", "itertools", "functools", "math", "random", "string", "time"}
NETWORK = re.compile(r"\b(urllib|requests|httpx|aiohttp|socket|websocket|boto3|openai|anthropic)\b")


def test_self_contained():
    print("\nno external dependencies — local markdown only")
    pyfiles = [p for p in ROOT.rglob("*.py") if ".git" not in p.parts]
    check("there are Python files to check", bool(pyfiles))

    for p in pyfiles:
        src = p.read_text(encoding="utf-8")
        mods = set()
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Import):
                mods |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                mods.add(node.module.split(".")[0])
        rel = p.relative_to(ROOT)
        check(f"{rel} imports only the standard library", not (mods - STDLIB_OK),
              f"third-party: {sorted(mods - STDLIB_OK)}")
        # Comments and question text may say "requests"; an import or a call may not.
        code = re.sub(r"#.*", "", src)
        hits = [m.group(0) for m in NETWORK.finditer(code) if re.search(
            rf"(import|from)\s+{m.group(0)}|{m.group(0)}\s*\.", code)]
        check(f"{rel} makes no network calls", not hits, f"{sorted(set(hits))}")

    # The storage contract, stated in backends.md and promised in both READMEs.
    backends = (SKILL / "references" / "backends.md").read_text(encoding="utf-8")
    check("backends.md describes local files only",
          not re.search(r"\b(notion|airtable|database|api key|oauth)\b", backends, re.I))
    for f in ("tracker.md", "ledger.md", "bank.md"):
        check(f"shipped course has {f}", (COURSE / f).exists())
    check("shipped course has a chapters folder", (COURSE / "chapters").is_dir())


# ---------- 5. the skill itself ----------

def test_skill():
    print("\nskill packaging")
    t = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    check("SKILL.md has frontmatter", t.startswith("---"))
    fm = t.split("---")[1]
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    check("frontmatter declares a name", bool(name))
    check("skill folder name matches the frontmatter name",
          bool(name) and name.group(1).strip() == SKILL.name,
          f"{name.group(1).strip() if name else '?'} vs {SKILL.name}")
    desc = fm.split("description:", 1)[1].strip() if "description:" in fm else ""
    check("description is within the 1024-char cap with headroom",
          0 < len(desc) <= 1000, f"{len(desc)} chars")

    for d in ("references", "assets/templates", "scripts"):
        check(f"{d}/ is present and non-empty", any((SKILL / d).glob("*")))

    # Every reference SKILL.md points at should exist — a dead pointer sends the model hunting.
    missing = [m for m in re.findall(r"`(references/[a-z-]+\.md)`", t) if not (SKILL / m).exists()]
    check("every references/ file SKILL.md names exists", not missing, f"{missing}")

    # The config the skill tells people to copy must actually be there.
    for m in re.findall(r"`(assets/templates/[a-z]+\.md)`", t):
        check(f"{m} exists", (SKILL / m).exists())


def test_config_privacy():
    print("\nlearner privacy")
    example = COURSE / "config.example.md"
    check("the tracked config is the .example template", example.exists(),
          "config.example.md is what ships; ai-pm-course.config.md is the learner's gitignored copy")
    if example.exists():
        text = example.read_text(encoding="utf-8")
        check("shipped config template has no filled-in details",
              "<" in text and ">" in text, "looks filled in — it may carry personal details")
        check("config template tells you to copy it before editing",
              "cp course/config.example.md" in text)
    live = COURSE / "ai-pm-course.config.md"
    check("a real filled-in config is not committed", not live.exists(),
          "course/ai-pm-course.config.md is present — it should be gitignored, not tracked")
    gi = (ROOT / ".gitignore").read_text(encoding="utf-8")
    check("a forker's filled-in config is gitignored by default",
          re.search(r"^\s*course/ai-pm-course\.config\.md\s*$", gi, re.M) is not None,
          "the live config is tracked — a forker who fills it in publishes their job search")


def main():
    bank = (COURSE / "bank.md").read_text(encoding="utf-8")
    ledger = (COURSE / "ledger.md").read_text(encoding="utf-8")
    tracker = (COURSE / "tracker.md").read_text(encoding="utf-8")

    test_generated()
    test_bank_ledger(bank, ledger, tracker)
    test_licence_promise(bank)
    test_self_contained()
    test_skill()
    test_config_privacy()

    print(f"\n{CHECKS - len(FAILURES)}/{CHECKS} checks passed")
    if FAILURES:
        print("failed: " + ", ".join(FAILURES))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
