---
name: ai-pm-course
license: MIT
description: Run an AI PM interview-prep coaching course from a question bank of markdown files — chapter (notes + web-verified currency + Evidence Bank) → MCQ quiz in chat → drill block scored on a 10-point rubric → bookkeeping in a local tracker and coverage ledger. Commands: start / resume / stop a sitting, "next chapter", "course status", "delta check", and first-run setup. Ships a 243-question bank and 34-chapter curriculum. The learner is mid-course and speaks in shorthand — treat a bare "chapter N", "next chapter", "run a cycle", "quiz me on RAG", "drill me", "course status", "delta check", "bank updated", or any mention of their question bank, tracker, or coverage ledger as this course, even if the message never says AI, PM, or interview. Use for ANY request to start, continue, run, check on, or set up AI / ML / LLM product-manager interview prep. Not for general AI explanations, work projects, resumes, or cover letters. The tracker is the memory — read it first.
---

# AI PM Course — cycle runner

A coaching loop for someone preparing for AI product-manager interviews. The course is built around a **question bank** — every question they might be asked — and exists so they can answer all of it well. One cycle ≈ 45 minutes: **chapter (10–15 min read) → MCQ quiz live in chat → drill block, answered aloud → bookkeeping**.

Sessions have no memory. Four markdown files are the memory:

| File | What it holds |
|---|---|
| `bank.md` | the questions, in the learner's own structure |
| `tracker.md` | curriculum, standing rules, Delta queue, Delta checks, drill ledger, cycle log |
| `ledger.md` | one row per bank question with its coverage status |
| `chapters/` | the chapters as they're built |

Everything worth keeping is written back to them *during* the cycle — that is what makes "never repeat a drill" and "am I improving?" possible. Nothing about the learner is hardcoded here: their name, targets, weak spots, embargoes and stale-fact traps live in a **config file** they keep (`references/config.sample.md` shows the shape).

## Step 0 — Load the config, then the memory

**Find the config**, in this order, stopping at the first hit:

1. Attached or pasted in this conversation.
2. `ai-pm-course.config.md` (or any `*course*config*.md`) in the working folder, the `course/` folder, or a connected folder.
3. None found → first run. Follow `references/setup.md`.

Never ask the learner to re-type something the config already holds. If you need a fact that isn't there, ask once and offer to add it.

A **config with `<placeholder>` fields still in it** is a fresh clone, not a broken setup. Treat those fields as empty, mention once in the opening line what's missing and offer to fill it, and get on with the cycle — nothing in a normal cycle needs their name. The exception is a placeholder in the file paths: without those you can't find the memory, so ask before doing anything else.

**Load the memory** from the paths in config: tracker, ledger, bank (`references/backends.md` covers the file mechanics). Then state where they are in one line — `Ch 7 next · 41/243 drilled · last cycle 6.8/10 · 2 in Delta queue` — and confirm the mode below. Don't narrate the loading.

## Modes

| The learner says | Do |
|---|---|
| `start`, `start day N` | Open a study sitting and show the plan for it, then begin — `references/sessions.md` |
| `resume` | Re-open the last unfinished sitting and continue from its bookmark — `references/sessions.md` |
| `stop` | Close the sitting, leaving a bookmark `resume` can act on — `references/sessions.md` |
| "next chapter", "run a cycle", "chapter N" | Full cycle: Steps 1 → 4 |
| "build chapter N", "chapter only" | Step 1 + its bookkeeping |
| "quiz me on X" | Step 2 (build or locate the chapter first if it doesn't exist) |
| "drill me", "drill block" | Step 3 + its bookkeeping, then Step 4 |
| "course status" | Status report (below); read-only |
| "delta check", "bank updated", or the cadence config sets | Delta check (below) |
| "set up the course", "start from scratch", or no config found | `references/setup.md` |

`start` / `resume` / `stop` wrap the sitting; the cycle steps below are what happens inside it. A learner who just says "next chapter" without `start` gets a cycle and no session row — that is fine, sessions are opt-in.

## Step 1 — Build the chapter

Use the fixed shape in `references/chapter-template.md`. The shape is fixed because chapters left to judgment drift between a five-minute skim and a thirty-minute wall, and the closing sections that make a chapter usable in an interview room (Evidence Bank, Question map) are the first thing dropped.

- **Spine** from the notes source in config, if there is one. Without notes, build from the web and general knowledge — say so, and lean harder on verification.
- **Freshness pass** — only for claims that rot *and* matter to this chapter's questions (3–8 of them): model lineup, pricing, context windows, framework landscape, regulation, named incidents. Verify each live, at build time, and put it in the Currency table with a source and **"as of \<Month YYYY\>"**. Unverifiable → mark ⚠ unverified. Never guess. No general news — currency is strictly topical to the chapter. Check the config's **stale-fact traps** before publishing: they are facts that were wrong once and will tempt you again.
- **Library layer** — if config names a reading list, fold in the 1–2 best pieces with links.
- **Evidence Bank** and **Question map** — the parts the learner will actually say out loud. Most often dropped, least skippable.
- Run the template's **build checklist**, then save as `chapters/ch-NN-<slug>.md` and give the learner the path.
- **Bookkeeping now, not later:** flip 📖 on every ledger row in the Question map; set the tracker row to `📖 <date>`.

## Step 2 — MCQ quiz (live in chat)

5–10 scenario- and trap-based questions — applied judgment, never definition recall (trap types and format in `references/grading-rubric.md`). Present them all, wait for the learner's answers, then score **X/N** and name the trap behind every miss in one line. Keep the score for the log line.

## Step 3 — Drill block (live, aloud)

3–5 bank questions from this chapter, Delta-queue items first if any are queued. **Never re-ask a ✅ question** — check the ledger before choosing. Ask one at a time; grade before moving on.

Grade every answer with the rubric in `references/grading-rubric.md`: five dimensions × 0–2 = a score out of 10, shown as a table with what earned and what lost points. Prose-only feedback is what makes progress invisible run to run; the numbers are the point.

- **Gate:** a 0 on any dimension listed under the config's **diagnosed misses** caps the answer at 5/10. Those habits are the reason the course exists; an answer that is brilliant except for the exact habit being trained is a failed rep, and the interviewer will see the habit, not the brilliance.
- **Multi-part questions:** hold the learner to every part. A dropped half is Completeness 0, not "mostly there".
- **Evidence:** expect the chapter's Evidence Bank items to be deployed. When they aren't, say which item should have been.
- Bookkeeping per answer: score ≥ config's pass threshold → ✅ in the ledger with date and score; below it → stays 📖 so it can be drilled again. Add a drill-ledger line. Score ≥ 8 → log the answer into the bank per the config's convention. A Delta-queue item: fill its Drilled cell with date · score; remove the row once it passes the threshold, otherwise it keeps its place at the front of the next block.
- End by naming **the single biggest gap**: a dimension, the question where it cost the most, the one-line fix. Never "overall strong, maybe tighten X".

## Step 4 — Close the cycle

Print the close-out table and fill every row with the literal value written, or `—` if that step didn't apply:

| Item | Done | Written |
|---|---|---|
| Chapter saved | ✅ | `chapters/ch-12-eval-foundations.md` |
| Ledger 📖 flips | ✅ | Q112–Q117 |
| Ledger ✅ flips | ✅ | Q112 (8), Q114 (7); Q113 stays 📖 (4) |
| Tracker row status | ✅ | `✅ 26 Aug · quiz 7/8 · 3 drilled · 6.3/10` |
| Cycle log line | ✅ | (the line) |
| Bank entries | — | none ≥ 8 |
| Delta queue | ✅ | 1 drilled, removed |

Then **verify by re-reading**: `python3 <skill>/scripts/course_tools.py verify --tracker <path> --ledger <path> --chapter N`, where `<skill>` is this skill's own folder (the script sits at `scripts/course_tools.py` inside it). Use `python3` — `python` is often not on PATH. A ❌ in this table isn't the failure — leaving it unrepaired is: the next cycle would re-drill or skip on the strength of what the tracker says.

Cycle log line format: `<date> · Ch N · quiz x/y · drilled n · mean s/10 · C/E/F/D/S a/b/c/d/e · gap: <dimension — Q-id>`.

If a Session row is `open` or `paused`, closing the cycle also closes it: Status → `done`, Updated refreshed, Next → `start Ch N+1`. A row left live after a finished cycle blocks the next `start` (`references/sessions.md`).

## Course status

Read-only. One table, under twelve lines: chapters by status, ledger counts by glyph, the last three cycle-log lines with their dimension scores and the trend, Delta-queue size, next chapter. If a Session row is `open`, add one line naming the sitting and its Next, so a learner who lost their place can find it without starting anything. `python3 <skill>/scripts/course_tools.py status --tracker <path> --ledger <path>` gives you the counts.

## Delta check

Diff the bank against the ledger — `python3 <skill>/scripts/course_tools.py delta --bank <path> --ledger <path>` lists candidates; the triage is yours. For every bank question with no ledger row:

| Finding | Action |
|---|---|
| Rephrase of an existing entry | Propose merging (keep the sharpest phrasing, credit the source); edit the bank only after an OK — until then it gets no ledger row |
| New, topic already covered (chapter ✅) | Ledger row 🆕 under its home chapter **and** a row in the tracker's Delta queue, so it's drilled first in the next block |
| New, future topic (chapter not yet ✅) | Ledger row 🆕 under its home chapter; the chapter build will pick it up |
| Out of scope | Ledger row ⛔ |

Every bank question ends up with exactly one ledger row (next free Q-id) — otherwise the next check re-flags it.

Then add a row to the tracker's **Delta checks** table — date · +new · merged · queued · ⛔ · notes — counting only this check; merges still awaiting an OK go in the notes, not in the count. Bump the Questions count of any chapter that gained a 🆕 row. Don't invent new tracker sections; if something has no home, it goes in that row's notes.

## Standing rules (every session)

- Config overrides this skill's defaults. Embargoes, out-of-scope topics and "do not nudge" items come from config — honour them without being reminded.
- **Ask twice before deleting anything.** Never restructure the bank or delete from it without an explicit OK.
- Never guess a rot-prone fact; date-stamp what you verified. When a stale fact is caught, offer to add it to the config's trap list.
- Tables over prose, lean output. The learner's time is the scarce resource; the chapter has a word budget for that reason.
- Interactivity is real: the quiz and drills wait for the learner. Never answer for them or grade an answer they didn't give.

## Files

- `references/config.sample.md` — every config field, filled in for a fictional learner.
- `references/chapter-template.md` — the chapter shape, word budget, build checklist.
- `references/grading-rubric.md` — MCQ format and trap types; the 5-dimension drill rubric, gate rule, score bands, per-answer and scorecard formats.
- `references/backends.md` — the data model, status glyphs, and file mechanics.
- `references/setup.md` — first-run flow, for the shipped starter pack or the learner's own bank.
- `references/sessions.md` — `start` / `resume` / `stop`: the Session bookmark and how to write it.
- `assets/templates/` — blank tracker, ledger, bank and config.
- `scripts/course_tools.py` — `status`, `next`, `sitting`, `verify`, `delta` (stdlib only; run with `python3` and the skill-relative path). `sitting` prints the live session bookmark, which is what `resume` needs.
