# SPAR grading evaluation plan

**Question.** Does the same answer receive comparable feedback across runs, and do the scores match an independent human assessment?

1. Prepare 12 fictional answers across four original AI PM prompts. Include strong, mixed, and weak answers, with deliberate variation across the five rubric dimensions. Fix the prompts, answers, and rubric before running the evaluation.
2. Score each answer independently against the 0–2 rubric. Record a short reason for each score and keep the human scores hidden from the model. Ask a second reviewer to score disputed examples where possible.
3. Grade each answer in three fresh sessions with the same model, skill revision, and settings. Record the version, total, five dimension scores, and cited evidence. Use the default rubric without personalized caps for the initial benchmark, then exercise the cap separately with fixtures that should and should not trigger it.
4. Report exact per-dimension agreement across runs and with the human reference. Report mean absolute total-score error, counts within one point, and any two-point dimension disagreements. Include sample size and examples of disagreement.
5. Review which dimensions drift and revise ambiguous anchors. Rerun with fresh examples before making a claim about scoring consistency.

This is a proposed benchmark. The walkthrough scores are illustrative and should stay separate from benchmark results.
