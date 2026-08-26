# Data model and file mechanics

The course's memory is three markdown files plus a folder. `assets/templates/` shows the exact layouts, `scripts/course_tools.py` parses them, and the shipped `course/` folder is a working example of all of it.

## The files

| File | Holds | Who writes it |
|---|---|---|
| **tracker.md** | Curriculum table (`#`, Chapter, Questions, Status) · Standing rules · Delta queue · Delta checks · Drill ledger · Cycle log | The skill, every cycle |
| **ledger.md** | One row per bank question: `Q-id`, Question, Home chapter, Status, Drilled (date), Score | The skill, every cycle |
| **bank.md** | The learner's questions, in their own structure | The learner. The skill only **appends** model answers (per config's convention) and **proposes** merges — it never restructures or deletes without an OK |
| **chapters/** | `ch-NN-<slug>.md`, one per chapter | The skill, on build |

### Structure is fixed

The tracker has exactly these sections: Curriculum · Standing rules · Delta queue · Delta checks · Drill ledger · Cycle log. Every session writes into those tables in their existing row format. Adding sections, legends or free-text notes to the tracker or ledger makes the next session — and `course_tools.py` — guess at the layout; if something has no home, it belongs in a Notes cell.

**An existing tracker may predate this layout** — bullets where the templates use tables, "Log" instead of "Cycle log", no Questions column, extra sections the learner wrote themselves. Follow the learner's layout and conventions; never restructure a tracker someone is already using. The one addition worth making is a **Delta checks** table if none exists, and say so when you add it.

The curriculum's **Questions** column (where present) is the live count of ledger rows with that home chapter (🆕 included, ⛔ excluded). A delta check that adds a 🆕 row bumps it; nothing else changes it.

### Status glyphs (ledger rows)

| Glyph | Meaning |
|---|---|
| ⬜ | not covered yet |
| 📖 | chapter read (or drilled below the pass threshold — eligible to drill) |
| ✅ | drilled to standard (score ≥ config's pass threshold) |
| 🆕 | new since baseline — added by a delta check, not yet covered |
| ⛔ | out of scope |

### Tracker row status format

`⬜` → `📖 26 Aug` → `✅ 26 Aug · quiz 7/8 · 4 drilled · 7.2/10`. Same string shape every time, so a status report can parse it and the learner can scan it.

### Cycle log line

`26 Aug 2026 · Ch 12 · quiz 7/9 · drilled 4 · mean 6.5/10 · C/E/F/D/S 1.5/0.8/1.3/1.8/1.3 · gap: E — Q115`

### Q-ids

`Q001`, `Q002`, … assigned once at setup in bank order; new questions from delta checks take the next free number. Q-ids are how the Question map, ledger, drill ledger and log refer to the same question without repeating its text. They are never renumbered — a Q-id is a permanent handle.

---

## Writing

- **Read**: open the files with the file tools. Paths come from config and are relative to the folder the config sits in.
- **Chapter**: write `chapters/ch-NN-<slug>.md` (two-digit N).
- **Ledger flips**: edit the row's Status / Drilled / Score cells in place. Keep row order — the ledger is in bank order and stays that way.
- **Tracker row**: edit the Status cell of the chapter's row in the curriculum table.
- **Log / queue / delta checks / drill ledger**: append a row to the relevant table.
- **Bank**: append the model-answer block under the question, in the shape config describes.
- **Verify**: `python3 <skill>/scripts/course_tools.py verify --tracker <path> --ledger <path> --chapter N` prints the tracker row, that chapter's ledger rows, and the last log line — paste the relevant lines into the close-out table. `status`, `delta` and `next` are the other subcommands; run any of them with `--help`.

`<skill>` is this skill's own folder; the script is at `scripts/course_tools.py` inside it. Use `python3` — plain `python` is often not on PATH. `--chapter` takes `4`, `Ch4` or a session code like `S25`.

Edit these files with a tool that reads and rewrites them (an editor, `sed -i`, a short read-modify-write script) — never by re-typing a file's contents from earlier output, which may have been truncated. A 243-row ledger does not survive being retyped from memory.

## Where the files live

- **Claude Code / a terminal**: the repo folder. Version them with git — the tracker and ledger are a genuinely useful commit history of what was learned.
- **Cowork with a connected folder**: work on the files in place on the machine; say which folder and file changed.
- **claude.ai with no file access**: the learner attaches the files and gets updated ones back to download. It works, but it is the weakest mode — every cycle is a manual round-trip. Suggest a folder or a repo if they'll be doing this often.

## A note on backups

The tracker and ledger accumulate months of work and nothing else holds it. A git repo makes that free. If the learner isn't using one, suggest it once at setup, then leave it alone.
