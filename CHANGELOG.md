# Changelog

## 1.0.0 — 14 September 2026

First public release, as **SPAR** — *Structured Practice for AI Roles*. The skill itself stays
`ai-pm-course`: a skill's name is a triggering signal, and a codename is not one.

**Added**

- 243-question Master Question Bank merged from nine published AI PM question lists, every
  question credited to its sources. The sources' own answer guidance and named frameworks are
  deliberately not reproduced — `LICENSE-CONTENT` states this, and `tests/run_tests.py` now
  enforces it rather than leaving it as a promise.
- 34-chapter curriculum plus 3 optional end sessions, and a coverage ledger with one row per
  bank question.
- `skill/ai-pm-course` — the coach: chapter build with a dated freshness pass, MCQ quiz,
  rubric-scored drill block, and bookkeeping that is re-read to prove it happened.
- `scripts/course_tools.py` — `status`, `next`, `sitting`, `verify`, `delta`. Read-only.
- `tools/build_course.py` — regenerates `bank.md` and `ledger.md` from one source list so their
  question text is byte-identical, with `--check` to verify it.
- `tests/run_tests.py` — 40 checks over the generated files, the bank/ledger invariant, the
  licence promise, the stdlib-only guarantee and learner privacy.
- GitHub Actions: CI on every push and PR; a release workflow that attaches the packaged
  `.skill` to a tagged release.
- `tools/package_skill.py`, `QUICKSTART.md`, `KNOWN-ISSUES.md`.

**Fixed**

- A forker who filled in `course/ai-pm-course.config.md` would have committed their name,
  target roles and diagnosed weak spots. The template now ships as `course/config.example.md`
  and the filled-in name is gitignored by default. A test fails if that protection is removed.
- The skill description was exactly 1024 characters — on the cap, with no room to add a trigger
  phrase. Trimmed to 972.

**Changed**

- Default branch is `main`.
