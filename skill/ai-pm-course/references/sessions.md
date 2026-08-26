# Sessions — start, resume, stop

Three commands wrap the study sitting itself. They exist because a 45-minute cycle rarely survives contact with a working day: the learner gets pulled into a meeting halfway through a drill block, comes back two days later, and neither of you remembers which questions were already asked. The tracker records *completed* cycles; the **Session** table records the sitting in progress.

This is cheap to support, because the course already writes bookkeeping per answer rather than at the end. When a sitting stops mid-block, every score so far is already in the ledger and the drill ledger. The bookmark only records **position**, never results — so a lost or stale bookmark can never cost the learner a grade.

## The Session table

Lives in the tracker, one row per sitting, newest last:

```markdown
## Session

| Day | Started | Updated | Status | Chapter | Step | Done this sitting | Next |
|---|---|---|---|---|---|---|---|
| 7 | 24 Aug 08:30 | 24 Aug 09:15 | done | Ch 1 | closing | quiz 6/8 · Q001 (7) · Q002 (6) | start Ch 2 |
| 8 | 26 Aug 09:10 | 28 Aug 08:40 | paused | Ch 2 | drills | quiz 7/9 · Q007 (6) · Q008 (5) | drill Q009, Q010, then close the cycle |
```

| Column | Means |
|---|---|
| **Day** | The numbered unit of work. `start` takes the next number; **`resume` keeps the same number** — a sitting picked up on Thursday is still the sitting begun on Tuesday. So Day counts work units, not visits and not calendar days. |
| **Started** / **Updated** | When the row was opened, and when it was last touched. `stop` and `resume` both refresh Updated, which is where the elapsed-time figure in a summary comes from. |
| **Status** | `open` · `paused` · `done`. See below — getting this right is what makes `resume` work. |
| **Step** | `chapter`, `quiz`, `drills`, or `closing`. |
| **Done this sitting** | Enough to avoid repeating work: the quiz score, and each Q-id drilled with its score. |
| **Next** | A plain-English instruction to your future self. This is the field `resume` acts on — write it as if the reader has no other context, because they don't. |

### The three states

| Status | Means | Set by |
|---|---|---|
| `open` | A sitting is live right now. | `start` |
| `paused` | Stopped part-way. **There is something to resume.** | `stop`, when the cycle isn't finished |
| `done` | Finished. Nothing to resume. | `stop` on a completed cycle, or Step 4 closing a cycle |

At most one row may be `open` **or** `paused` at a time. `done` rows accumulate as a history.

The distinction between `paused` and `done` is the whole mechanism. A `closed`-for-everything status would make `resume` unable to tell "you have half a drill block waiting" from "you finished, start something new".

## `start` — open a sitting

Takes an optional day number: `start`, `start day 12`, `start 12`.

1. Run Step 0 (config, then memory) as normal.
2. **If a row is `open` or `paused`, do not open another.** Say what's waiting and run `resume` instead — two live sittings is how a drill block gets asked twice.
3. Work out the day number: the one given, or the last Day + 1, or 1 if the table is empty. A day number that already exists means they want that sitting back: treat it as `resume` on that row and say so.
4. Append a row: Day, Started and Updated set to now, `open`, the chapter you're about to work on, its step, empty Done, and the first action in Next.
5. Show the **plan for the sitting** — this is what makes `start` worth typing over "next chapter":

```
Day 8 · 28 Aug · ~45 min

Ch 12 — Eval foundations   (chapter built 26 Aug, 5 of 7 drilled)
Owed first:   Q113 (6/10, below your threshold) · Q131 from the Delta queue
Then:         Q115, Q117
Close with:   the cycle log line — this finishes Ch 12

Last cycle: 6.8/10 · weakest dimension E (0.8)
```

Then begin. Don't wait for a further go-ahead — `start` *is* the go-ahead.

## `resume` — pick up where they left off

1. Step 0 as normal.
2. Find the last row whose Status is `open` or `paused`. If there is none, say so in one line and run `start` instead — no ceremony. (`python3 <skill>/scripts/course_tools.py sitting --tracker <path>` prints exactly this row, if you'd rather read it than parse the table.)
3. Set Status back to `open`, refresh Updated, **keep the Day number**, and restate the bookmark in **one line** so the learner can correct you before you act on it:

```
Resuming Day 8 · Ch 12 · drills · done: Q113 (6) · next: Q115, then close the cycle.
```

4. Continue from exactly that point. Do not rebuild the chapter, re-run the quiz, or re-ask any Q-id in Done. If the chapter file is missing, say so and offer to rebuild rather than silently starting over.
5. If the bookmark is stale — the ledger shows questions drilled that Done doesn't list — trust the **ledger**, say which one you trusted and why, and repair the bookmark. The ledger is the record; the bookmark is a convenience.

## `stop` — close the sitting

The learner may say this at any point, including mid-question. Stop cleanly rather than racing to finish the step.

1. Finish grading the answer in flight, if there is one, and write its bookkeeping. Never leave an answer graded in chat but unrecorded.
2. Update the row: refresh Updated, Done and Next, and set Status:
   - the cycle still has work in it → **`paused`**, with Next naming the first thing to do next time;
   - the cycle is complete → run Step 4's close-out properly, then **`done`**.
3. Give a short sitting summary, then get out of the way:

```
Day 8 paused · 22 min today
Drilled: Q113 6/10 · Q115 7/10
Today's gap: E — Q113 still leaning on "studies show" rather than a dated number.
Next time: Q117, then the cycle log line closes Ch 12. Say `resume`.
```

No encouragement, no "great work today". The numbers say whether it was a good sitting.

## When a cycle finishes without `stop`

Most sittings end by finishing the cycle, not by the learner typing anything. **Step 4 owns this**: when the close-out table is done, if a row is `open` or `paused`, set it to `done`, refresh Updated and Next (`start Ch N+1`). A row left `open` after a finished cycle blocks the next `start`.

## Sessions vs cycles

A **cycle** is a unit of course content: one chapter, read, quizzed, drilled, logged. A **session** (or sitting) is a unit of the learner's time. One sitting may hold two cycles, or a third of one. They are tracked separately because progress reporting cares about cycles and the learner's calendar cares about sittings.

`course status` reports both: chapters done from the curriculum, and — when a row is `open` or `paused` — one line naming it and its Next, so a learner who has forgotten where they were can find out without starting anything.

## The "optional sessions" name clash

The curriculum's optional end sessions (S25–S27, the behavioural Story Labs) are course content, unrelated to study sittings. When both could be meant, call the time-based one a **sitting**. The status report already does.
