# SPAR — Quickstart & command reference

*Structured Practice for AI Roles.* You are reading this from inside the skill, so it is
probably already installed. Skip to [Commands](#commands) if so.

---

## Install

**Claude Code** — copy this folder into `~/.claude/skills/` (or a project's `.claude/skills/`).
**Claude desktop / web / Cowork** — attach the `.skill` file and click **Save skill**.
**Codex** — copy this folder into `~/.agents/skills/` (or a repo's `.agents/skills/`).

Python 3.9+ is the only requirement. Nothing to `pip install` — this skill is standard library
only, and a test in the repo fails if that ever changes.

## Set up the course

You need four markdown files: a question bank, a tracker, a ledger, and a config. The
[repo](https://github.com/HelloIamChetan/spar-ai-pm-course) ships all four ready to go — a
243-question bank, a 34-chapter curriculum plus 3 optional end sessions, and a ledger with every
question indexed.

```bash
git clone https://github.com/HelloIamChetan/spar-ai-pm-course.git
cd spar-ai-pm-course
cp course/config.example.md course/ai-pm-course.config.md
```

Open your copy, set your name, target role and timing. **Leave *Diagnosed misses* empty** — the
course proposes them from your own scores after two cycles, which beats guessing on day one.
Your copy is gitignored, so filling it in can't publish your job search.

Bringing your own questions instead? Say `set up the course` and it builds the curriculum,
tracker and ledger from your bank — `references/setup.md` has the detail.

Then open Claude in that folder and say `start`.

---

## Commands

You talk to it in plain language; these are the phrasings it recognises.

### Running a sitting

A **sitting** is a unit of your time. A **cycle** is a unit of course content. They don't line
up one to one — a good sitting might be two cycles, or half of one.

| Say | What happens |
|---|---|
| `start` | Opens a sitting, shows the plan, begins |
| `start day 3` | Opens a sitting against day 3 of a multi-day plan |
| `resume` | Re-opens the last unfinished sitting from its bookmark |
| `stop` | Closes the sitting, leaving a bookmark `resume` can act on |

### Running a cycle

One full cycle is about 45 minutes: chapter → quiz → drills → bookkeeping.

| Say | What happens |
|---|---|
| `next chapter` · `run a cycle` | Full cycle on the next chapter in the curriculum |
| `chapter 12` | Full cycle on that chapter specifically |
| `build chapter 12` · `chapter only` | Just the chapter, plus its bookkeeping |
| `quiz me on RAG` | Just the quiz (builds or finds the chapter first) |
| `drill me` · `drill block` | Just the drills, then the bookkeeping |

### Checking in

| Say | What happens |
|---|---|
| `course status` | Where you are, and whether your scores are actually moving. Read-only |
| `delta check` · `bank updated` | Re-indexes the ledger after you edit the bank |
| `set up the course` · `start from scratch` | First-run setup |

Shorthand works. A bare `chapter 7` or `drill me` is enough — you don't have to say "AI PM
course" for it to know what you mean.

### The scripts

The skill runs these itself; run them by hand when you want a number without opening a session.
All are read-only — they never write to your files.

```bash
SKILL=~/.claude/skills/ai-pm-course

python3 $SKILL/scripts/course_tools.py status  --tracker course/tracker.md --ledger course/ledger.md
python3 $SKILL/scripts/course_tools.py next    --tracker course/tracker.md
python3 $SKILL/scripts/course_tools.py sitting --tracker course/tracker.md
python3 $SKILL/scripts/course_tools.py verify  --tracker course/tracker.md --ledger course/ledger.md --chapter 4
python3 $SKILL/scripts/course_tools.py delta   --bank course/bank.md --ledger course/ledger.md
```

| Subcommand | Prints |
|---|---|
| `status` | Chapter and ledger counts, what's next, the live sitting, the delta queue |
| `next` | The next unread chapter, as `N<tab>title` |
| `sitting` | The open sitting, if there is one |
| `verify` | One chapter's tracker row, its ledger rows and the last log line |
| `delta` | Bank questions missing from the ledger, and ledger rows with no bank match |

`--chapter` takes `4`, `Ch4`, or a session code like `S25`. `delta` takes `--threshold` (default
0.85) to tune how close two questions must be before it calls them the same question.

---

## Your files

| File | Holds | Who writes it |
|---|---|---|
| `bank.md` | Your questions | You. The skill only appends answers and *proposes* merges |
| `tracker.md` | Curriculum, sitting, delta queue, drill ledger, cycle log | The skill, every cycle |
| `ledger.md` | One row per bank question with its coverage status | The skill, every cycle |
| `chapters/` | `ch-NN-<slug>.md` as they're built | The skill, on build |

All local markdown. No database, no account, nothing leaves your disk. Commit them — the tracker
becomes an honest record of what you learned and where you're still weak.

### Status glyphs

⬜ not covered · 📖 chapter read, or drilled below the pass threshold · ✅ drilled to standard ·
🆕 new since the baseline · ⛔ out of scope

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| "It didn't find my config." | It looks for `ai-pm-course.config.md` (or any `*course*config*.md`) in the working folder, a `course/` folder, or a connected folder — and accepts one attached to the conversation. Did you copy the template, or only edit it in place? |
| Placeholders still in the config | Fine. A `<placeholder>` means a fresh clone, not a broken setup — nothing in a normal cycle needs your name. |
| `chapters/` is empty | Intended. Chapters are built per learner and per run, so a shipped one would be stale. |
| A delta check re-flags questions already indexed | The ledger text drifted from the bank. Run `python3 tools/build_course.py --check` in the repo. |
| Drill scores feel harsh | They're comparable, not calibrated. The trend across cycles is the signal; the absolute number isn't a prediction. |

More: `README.md` in this folder · `references/` for the rubric, the data model, sessions and setup.
