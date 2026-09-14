# Known issues

Things this repo knows are limited or missing. Stated rather than papered over — the same
standard the drill rubric holds you to.

## Chapters are not shipped

`course/chapters/` ships empty on purpose. Chapters are built per learner and per run, and the
freshness pass verifies rot-prone facts (model lineups, pricing, context windows) on the day you
build, so two people running chapter 5 a month apart should get different Currency tables. A
shipped chapter would be stale within weeks and would read as authoritative anyway.

Consequence: a fresh clone has the bank, the ledger and the curriculum, but no reading material
until you run a cycle. That is the intended shape, not a missing step.

## The freshness pass needs web access

Everything about your data is local markdown. But chapter *building* verifies a handful of
rot-prone claims live, and without web access those come back `⚠ unverified` rather than wrong.
The course still runs; the Currency table is just thinner. Nothing else in the skill touches the
network, and `tests/run_tests.py` fails if any script grows a network call.

## Three questions are out of scope

Q241–Q243 are software-engineering live-coding questions from AI company loops. They are indexed
`⛔` so the coverage maths doesn't pretend they're yours to drill, and so a delta check doesn't
re-flag them every time. If you want them, change the status.

## Behavioural questions sit outside the core 34

26 behavioural, cross-functional and career questions live in the three optional end sessions
(`S25`–`S27`) rather than in a chapter, because they need your own stories, not content. They are
in the ledger and they count toward the 243 — they're just not drilled in technical blocks.

## The bank is a snapshot of nine published lists

Collected in August 2026. Interview questions drift as the field does. When you find new ones,
add them to `course/bank.md`, say "delta check", and the ledger re-indexes what moved — that flow
is the maintenance story, and it's why the ledger must match the bank byte for byte.

## Scores are comparable, not calibrated

The 10-point rubric is the same every cycle, so *your* trend line is meaningful. The absolute
number is not a prediction of how a real interviewer would score you.
