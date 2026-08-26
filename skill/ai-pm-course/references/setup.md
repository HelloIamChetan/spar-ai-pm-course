# First-run setup

Run this when no config is found, or when the learner asks to set up / start the course. If a config or tracker already exists, ask twice before replacing anything — a restart wipes months of ledger history.

There are two paths. Ask which one applies in the same message as everything else; most people take the first.

- **Path A — use the shipped course.** The repo's `course/` folder already has a 243-question bank, a 34-chapter curriculum plus 3 optional end sessions, and a ledger with every question indexed. Setup is one file: their config. Two minutes, then cycle 1.
- **Path B — bring your own bank.** They have their own list of questions. You build the curriculum, tracker and ledger from it.

## 1. Gather — one message, not a drip of questions

Ask for everything at once; the learner can answer in one reply.

| Need | Why |
|---|---|
| **Path A or B** — use the shipped bank, or theirs (pasted, a file, a link) | Decides the rest of setup |
| **Course notes** (optional) — files they already have | The chapter spine comes from here. Without notes, chapters are built from the web and general knowledge — fine, but slower and needing more verification |
| **Target** — role level, kind of company (model lab, applied-AI product, big tech), interview timing if known | Sets depth and which topics get priority |
| **Where the files live** — a folder or repo path | Defaults to the repo's `course/` folder |
| **Cycle length** — default 45 min | Sizes the chapter and the drill block |
| **Off-limits and embargoes** — projects whose figures can't be quoted yet, topics they don't want, decisions they've reserved (mock interviews, paid platforms) | These go into config so no session has to be told twice |
| **Known weak spots** (optional) | Become the diagnosed misses — the gate in the rubric. If unknown, leave empty and diagnose after two cycles |

If they only answer some of it, use defaults for the rest and say which defaults you used.

## 2. Path A — shipped course

Nothing to build. Copy `skill/assets/templates/config.md` to `course/ai-pm-course.config.md`, fill in what they told you, and point the paths at the `course/` folder. Read back: 243 questions, 34 chapters + 3 optional sessions, where the files are, the config in ten lines. Offer cycle 1.

If they want to trim the course (they only have three weeks, or they only care about evals and agents), don't delete chapters — reorder the curriculum table and say which chapters they're skipping for now. Deleted rows lose the coverage record; skipped rows are still there when they have time.

## 3. Path B — build the curriculum from their bank

Cluster the bank into chapters ordered by dependency: fundamentals → systems (RAG, agents, fine-tuning) → evals and quality → product and metrics → cost and strategy → behavioural last, as **optional end sessions**. Every question gets exactly one home chapter.

**Size the chapter count from the bank, not the other way round.** A chapter needs 3–6 questions: fewer than three can't fill a drill block, more than six won't fit a 45-minute cycle. So a 30-question bank gives roughly 8–10 chapters; a 240-question bank gives 30–40. Merge rather than create a thin chapter, and say what the sizing rule produced.

**What counts as behavioural:** any question about the learner rather than the subject — their past ("tell me about a time…"), their motivation ("why AI PM?"), their plans ("first 90 days"), their working style, how they handle conflict. These go to the optional end sessions even when they sound strategic. Technical chapters drill judgment about systems; the end sessions drill positioning and stories, which need a different rubric and the learner's own material.

Show the proposal as a table — `#` · Chapter · Questions (count) · Why here — and get an OK before creating anything. Questions that don't belong in an AI PM course (investing, unrelated engineering trivia) get ⛔ in the ledger rather than a chapter; list them so the learner can object.

Then create, from `assets/templates/`:

- **tracker.md** — curriculum table filled in, every row `⬜`; standing rules = the skill's generic rules plus "see config"; Delta queue, Delta checks, drill ledger and cycle log empty.
- **ledger.md** — one row per bank question, `Q001…` in bank order, home chapter set, status `⬜` (or `⛔`). **Use the bank's exact question text** — the delta check matches ledger rows to bank questions by text, and a paraphrased ledger makes every future check flag questions that are already indexed.
- **bank.md** — save theirs where config points. Don't restructure it.
- **config.md** — filled from step 1, saved as `ai-pm-course.config.md` next to the tracker.

Every line in the learner's config, tracker and ledger comes from them or from the blank templates. `references/config.sample.md` is an illustration of the format, not a source: its embargoes, diagnosed misses, do-not-nudge items and stale-fact traps belong to a fictional learner and must not be copied in. A learner who inherits someone else's rules will be coached against habits they don't have.

## 4. Read back

Show: chapters created, questions indexed (and how many ⛔), where each file lives, the config in ten lines. Ask them to keep the config private if it holds anything sensitive. Then offer to run cycle 1.

## Diagnosing misses later

If config has no diagnosed misses, after two completed cycles look at the per-dimension means in the cycle log. Propose the 1–3 lowest dimensions as diagnosed misses, with the questions where each showed, and offer to add them to config. That turns on the rubric's gate. Revisit every ten cycles: a miss that has scored 2 for five cycles running has been fixed and should come off the list.
