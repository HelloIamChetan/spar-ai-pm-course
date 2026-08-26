# Contributing

The most valuable contribution is **a real question you were actually asked**, with the company and roughly when. That is what keeps the bank honest — everything else in it came from published lists.

## Adding questions

1. Add the question to `tools/build_course.py` in the right section, with a home chapter and a source code.
2. Run `python tools/build_course.py` to regenerate `course/bank.md` and `course/ledger.md`.
3. Run `python tools/build_course.py --check` — it should pass.
4. Open a PR saying where the question came from.

Please don't hand-edit `course/bank.md` or `course/ledger.md` in a PR; they're generated, and hand edits drift the two apart, which breaks delta checks for everyone.

Keep chapters between 4 and 9 questions. If a chapter is getting fat, propose a split rather than piling on.

## Adding source guidance

Please don't. The bank credits nine authors and deliberately excludes their answer guidance and named frameworks — that's their work, and reproducing it here would be repackaging paid material. Questions and credits only.

## Improving the coach

`skill/ai-pm-course/` is the skill. Changes to the rubric or the chapter template affect everyone's scores, so explain the reasoning in the PR and, ideally, show a before/after on a real drill answer.
