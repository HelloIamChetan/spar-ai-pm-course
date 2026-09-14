# SPAR

**A coach for AI product-manager interview prep that keeps score.**

You bring a bank of questions you might be asked. The course turns it into a curriculum, then runs you through it one sitting at a time: it writes the chapter, quizzes you, drills you out loud, scores every answer against a fixed rubric, and writes down what happened — so six weeks in you can see that your Evidence score went 0.5 → 1.4 and your Decision score hasn't moved at all.

Everything lives in four markdown files you own. No database, no account, no lock-in.

---

## Install

Copy this folder into where Claude looks for skills:

```bash
mkdir -p ~/.claude/skills
cp -r ai-pm-course ~/.claude/skills/
```

Or, if you have the packaged `.skill` file, attach it in Claude and click **Save skill**.

Then either point it at the shipped course (a 243-question bank and 34 chapters, if you got this as part of the repo) or say `set up the course from my question bank` and give it your own list.

---

## Commands

### Running a sitting

| Command | What it does |
|---|---|
| `start` | Opens a study sitting. Shows the plan — which chapter, what's owed from last time, roughly how long — then begins. |
| `start day 12` | Same, but you're naming the day number. Re-using a day number re-opens that sitting instead. |
| `resume` | Picks up the last unfinished sitting exactly where it stopped. Won't re-ask a question you already answered. |
| `stop` | Pauses the sitting and leaves a bookmark. Safe mid-question — the answer in flight gets graded and recorded first. |

`start` and `stop` are optional. If you just say `next chapter` and work straight through, nothing breaks; you simply don't get a bookmark.

### Working through the course

| Command | What it does |
|---|---|
| `next chapter` | A full cycle: chapter → quiz → drills → bookkeeping. About 45 minutes. |
| `chapter 12` | The same, for a specific chapter. |
| `build chapter 9, skip the drills` | Chapter only — useful for reading on a commute. |
| `quiz me on RAG` | Just the quiz, on any topic in the course. |
| `drill me` | Just the drill block, from wherever you are. |
| `drill me on chapter 12, be harsh` | Drills from a specific chapter. |

### Keeping the books straight

| Command | What it does |
|---|---|
| `course status` | Where you are: chapters done, questions covered, your last three cycles with dimension scores and the trend, and any open sitting. Read-only. |
| `delta check` | After you've added questions to the bank: indexes the new ones, proposes merges for near-duplicates, marks anything out of scope. Never edits your bank without asking. |
| `set up the course from my question bank` | First-run setup from your own list of questions. |

---

## What one cycle looks like

**1 · Chapter.** A 10–15 minute read built to a fixed shape: core concepts, decision rules, a table of rot-prone facts verified on the web *that day* and date-stamped, 2–3 dated pieces of evidence you can actually cite in a room, and a map of exactly which bank questions this chapter answers.

**2 · Quiz.** 5–10 scenario questions with plausible traps — applied judgment, never definition recall. Scored, with the trap named on every miss.

**3 · Drills.** 3–5 bank questions answered out loud. Each gets a score out of 10 across five dimensions, with the specific phrases that earned and lost points quoted back at you.

**4 · Bookkeeping.** Ledger statuses flip, the tracker row and cycle log get written, and the coach re-reads the files to prove it happened — then shows you a close-out table with the literal values written.

### The rubric

| | 0 | 1 | 2 |
|---|---|---|---|
| **C** Completeness | part of the question unanswered | every part touched, one thin | every part answered at depth |
| **E** Evidence | no dated fact or number | a generic reference ("studies show") | a specific, dated, deployable item |
| **F** Framing | accepted the premise | named an assumption, then answered | challenged the premise first — compared to what, at what volume |
| **D** Decision & cost | an opinion, or a list of options | a recommendation with no cost | a costed proposal: what, how long, what we'd learn |
| **S** Structure | rambling | shape buried | headline → supports → close |

Dimensions are scored against their anchors first, then summed — never an overall impression back-filled into the boxes. That's what makes the numbers comparable week to week.

**The gate.** Once you've done a couple of cycles, list your one to three worst dimensions in your config as *diagnosed misses*. After that, a 0 on any of them caps the answer at 5/10 no matter how good the rest was — because in the room the interviewer sees the habit, not the brilliance.

---

## Your files

| File | What it is |
|---|---|
| `bank.md` | Your questions. Yours to edit — add, re-word, cut. Run `delta check` afterwards. |
| `ledger.md` | One row per question: home chapter, status, date drilled, score. The record of what you actually know. |
| `tracker.md` | Curriculum, session bookmark, delta queue, drill ledger, cycle log. |
| `chapters/` | Chapters as they're built. |
| `ai-pm-course.config.md` | Your settings — the only file with anything personal in it. |

Keep them in a git repo if you can. The tracker and ledger accumulate months of work and nothing else holds it.

### Status glyphs in the ledger

⬜ not covered · 📖 chapter read, ready to drill · ✅ drilled to standard · 🆕 new since the last delta check · ⛔ out of scope

A question drilled below your pass threshold stays 📖, so it comes back around. Nothing is marked done because you saw it once.

---

## Configuration

`ai-pm-course.config.md` holds everything personal. Nothing about you is hardcoded in the skill.

| Section | What it's for |
|---|---|
| Learner | Name, current role, target roles, interview timing, cycle length |
| Files | Where the tracker, ledger, bank and chapters live |
| Sources | Your own course notes, if you have any — the chapter spine comes from there |
| Diagnosed misses | Your one to three worst rubric dimensions. Leave empty at first; the course proposes them from your own scores after two cycles |
| Drill pass threshold | The score that earns a ✅. Default 5 |
| Embargoes & scope | Things the coach must honour without being reminded — a side project whose numbers aren't public yet, topics you don't want |
| Do not nudge | Decisions you've reserved for yourself, so nobody keeps suggesting them |
| Bank conventions | How your strong answers get appended to the bank |
| Stale-fact traps | Facts that were wrong once. Grows as you go — the coach offers to add a line whenever it catches one |

`references/config.sample.md` is a filled-in example for a fictional learner. It shows the format; it is **not** a source to copy from — its embargoes and misses belong to someone who doesn't exist.

---

## Command-line helper

`scripts/course_tools.py` reads your files and never writes to them. Stdlib only, no install.

```bash
python3 scripts/course_tools.py status  --tracker course/tracker.md --ledger course/ledger.md   # where you are
python3 scripts/course_tools.py next    --tracker course/tracker.md
python3 scripts/course_tools.py sitting --tracker course/tracker.md                             # the live bookmark
python3 scripts/course_tools.py verify  --tracker course/tracker.md --ledger course/ledger.md --chapter 12
python3 scripts/course_tools.py delta   --bank course/bank.md --ledger course/ledger.md
```

`--chapter` accepts `12`, `Ch12`, or a session code like `S25`.

---

## Troubleshooting

**"It didn't find my config."** The skill looks for `ai-pm-course.config.md` (or any `*course*config*.md`) in your working folder, a `course/` folder, or a connected folder — and it accepts one attached to the conversation. If none of those apply, attach it or say where it lives.

**"It started setup when I already have a course."** That means it couldn't find your config. Same fix. It will always ask twice before replacing an existing tracker.

**"It re-asked a question I already answered."** Check the ledger row — if the status is 📖 rather than ✅, the question was drilled below your pass threshold and is meant to come back. If it's ✅ and it still got asked, that's a bug worth reporting.

**"`resume` doesn't know where I was."** The Session table in the tracker is the bookmark; its Status column is `open`, `paused` or `done`, and `resume` looks for the last `open` or `paused` row. If every row says `done` there is genuinely nothing half-finished — say `start`. If the table is empty you never ran `start`; say `next chapter` and carry on, the ledger still knows which questions are done.

`python3 scripts/course_tools.py sitting --tracker course/tracker.md                             # the live bookmark` prints the live bookmark if you want to see it yourself.

**"A fact in the chapter looks wrong."** Chapters date-stamp anything that rots. If something's off, say so — the coach will offer to add it to your config's stale-fact traps so it doesn't come back.

**"The chapter is too long / too short."** The template targets 1,400–2,200 words. If your cycles are consistently overrunning, shorten `cycle length` in your config.

---

## Reference files

Written for the model, but readable if you want to know exactly what it's doing or want to change its behaviour:

| File | Covers |
|---|---|
| `SKILL.md` | The loop itself — the four steps and the standing rules |
| `references/sessions.md` | `start` / `resume` / `stop` and the session bookmark |
| `references/chapter-template.md` | The chapter shape, word budget, and build checklist |
| `references/grading-rubric.md` | Quiz trap types, the five dimensions, the gate, score bands |
| `references/backends.md` | The data model, status glyphs, and file mechanics |
| `references/setup.md` | First-run setup, from the shipped course or your own bank |
| `references/config.sample.md` | Every config field, filled in for a fictional learner |
| `assets/templates/` | Blank tracker, ledger, bank and config |

Editing the rubric or the chapter template changes everyone's scores in your history, so if you change them, note the date — the trend line either side of that edit isn't comparable.

---

## Limitations, honestly

- **The coach is a model, not an interviewer.** It grades consistently against a written rubric, which beats most practice partners. It can't read your face or improvise pressure the way a good human will. Build reps here; do the real thing elsewhere.
- **Chapters are generated fresh.** Rot-prone facts are verified at build time and date-stamped; the rest comes from the model. Check any number you plan to say out loud.
- **The bank is a snapshot.** Add real questions as you hear them — that's what `delta check` is for.
- **Behavioural questions need you.** The optional end sessions can structure your stories; nobody else can supply them.
