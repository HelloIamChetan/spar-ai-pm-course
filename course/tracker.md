# SPAR — Tracker

> Source of truth for where you are in the course. Personal settings live in `ai-pm-course.config.md`.

## Curriculum

| # | Chapter | Questions | Status |
|---|---|---|---|
| 1 | How an LLM is made — data, pre-training, post-training, weights, why it isn't a database | 6 | ⬜ |
| 2 | The runtime knobs — tokens, context window, temperature, embeddings, why identical prompts differ | 5 | ⬜ |
| 3 | Hallucination — why it happens, grounding, the exec explainer, the PM playbook | 6 | ⬜ |
| 4 | When NOT to use an LLM — classic ML vs LLM, hybrid systems, the four-layer AI product stack | 7 | ⬜ |
| 5 | RAG end to end — when to use it, the pipeline, chunking, embeddings, vector DBs | 7 | ⬜ |
| 6 | RAG in production — failure modes, retrieval vs generation evals, stale and permissioned docs | 7 | ⬜ |
| 7 | Context & prompt engineering — window budget and priority, prompt-as-versioned-spec, prompt chains | 4 | ⬜ |
| 8 | Tool calling & MCP — what actually happens, tool definitions, MCP vs one-off integrations | 5 | ⬜ |
| 9 | Agent design — agent vs chatbot, memory, when agents earn their place, the support-agent case | 7 | ⬜ |
| 10 | Agent safety & reliability — approvals, irreversible actions, failure recovery, compounding reliability | 7 | ⬜ |
| 11 | Orchestration & routing — frameworks vs raw SDK, model routing, multi-agent sequencing | 6 | ⬜ |
| 12 | Eval foundations — whiteboard a framework, eval sets with no production data, golden datasets | 7 | ⬜ |
| 13 | LLM-as-judge & non-determinism — judge failure modes, A/B without a single right answer | 4 | ⬜ |
| 14 | Defining success — north stars, the metric framework, connecting model quality to business outcomes | 7 | ⬜ |
| 15 | Metric cases — north stars for named products, and what to do when instrumentation dies | 7 | ⬜ |
| 16 | Debugging foundations — regressions after a model swap, observability, human-in-the-loop, trace evaluation | 6 | ⬜ |
| 17 | Diagnosing metric drops — engagement, CTR, session depth, task completion | 5 | ⬜ |
| 18 | Diagnosing quality complaints — post-update regressions, falling acceptance, "it feels stupid" | 5 | ⬜ |
| 19 | Designing AI features — the design structure, designing for wrong outputs, trust & verification | 6 | ⬜ |
| 20 | AI product judgment calls — where AI adds value, integration, feasibility vs user needs | 6 | ⬜ |
| 21 | Design cases — assistants and everyday agents | 7 | ⬜ |
| 22 | Design cases — high-stakes and guardrailed products | 7 | ⬜ |
| 23 | Growth cases & warm-ups — moving a number, and the classic non-AI design question | 8 | ⬜ |
| 24 | The cost-latency-quality triangle — reduction levers, stream/cache/batch, what you trade for what | 7 | ⬜ |
| 25 | Model selection — frontier vs small vs open-weights, routing by task, custom models | 7 | ⬜ |
| 26 | Unit economics & estimation — cost at 1M users, inference estimation, GPUs, routing economics | 8 | ⬜ |
| 27 | Launch gates & fallbacks — the 90%-accurate launch call, asymmetric harm, fallback design | 9 | ⬜ |
| 28 | Responsible AI & regulation — bias, PII, compliance, the EU AI Act, risk management | 6 | ⬜ |
| 29 | Adversarial & abuse — prompt injection, red-teaming, misuse at scale, government pressure | 6 | ⬜ |
| 30 | Redlines & capability policy — what is too dangerous to ship, capability vs safety trade-offs | 6 | ⬜ |
| 31 | Moats & build-vs-buy — defensibility when models commoditise, data flywheels, build/buy/fine-tune | 6 | ⬜ |
| 32 | Pricing & prioritization — pricing AI features, ranking investments, communicating value | 5 | ⬜ |
| 33 | Roadmapping under fast model improvement — what stays constant when capabilities move monthly | 5 | ⬜ |
| 34 | Builder mindset — prototyping in a week, no-code validation, what to hand engineering | 7 | ⬜ |

*Optional end sessions — behavioural and positioning questions. They need your own stories, so they are drilled differently and do not gate the technical chapters.*

| # | Session | Questions | Status |
|---|---|---|---|
| S25 | Position & POV — your take on AI, your tools, your journey | 8 | ⬜ |
| S26 | Story Lab I — shipping, outcomes, and things that went wrong | 9 | ⬜ |
| S27 | Story Lab II — working with engineers, scientists and stakeholders | 9 | ⬜ |

## Standing rules

- The config overrides defaults. Embargoes, scope and do-not-nudge items live there.
- Ask twice before deleting anything. Never restructure or delete from the bank without an OK.
- Never guess a rot-prone fact; date-stamp what was verified.
- Never re-ask a ✅ question.

## Session

*One row per study sitting. Status is `open` · `paused` · `done`. `start` appends an open row; `stop` sets `paused`, or `done` if the cycle finished; `resume` re-opens the last open-or-paused row and keeps its Day number. At most one row may be open or paused at a time.*

| Day | Started | Updated | Status | Chapter | Step | Done this sitting | Next |
|---|---|---|---|---|---|---|---|

## Delta queue

*New questions on already-covered topics, waiting to be drilled first in the next block.*

| Added | Q-id | Question | Source | Drilled |
|---|---|---|---|---|

## Delta checks

*One row per delta check, counting only that check. Merges still awaiting an OK go in Notes.*

| Date | +new | merged | queued | ⛔ | Notes |
|---|---|---|---|---|---|

## Drill ledger

| Date | Ch | Q-id | Score | Gate | Note |
|---|---|---|---|---|---|

## Cycle log

| Date | Ch | Quiz | Drilled | Mean | C/E/F/D/S | Biggest gap |
|---|---|---|---|---|---|---|
