# AI PM Course — Config (sample)

> This is a **filled-in example** for a fictional learner, so every field is shown with a realistic value. Your own config is private: copy `assets/templates/config.md`, fill it in, and keep it out of anything you share. The skill reads it at the start of every session and never edits it without asking.

## Learner
- name: Alex
- current role: Senior PM, payments platform at a mid-size fintech
- target: AI PM roles at applied-AI product companies and one or two model labs; interviews expected from October 2026
- cycle length: 45 min
- delta check cadence: first cycle of each week

## Files
<!-- Paths are relative to the folder this config sits in. -->
- tracker: ./tracker.md
- ledger: ./ledger.md
- bank: ./bank.md
- chapters folder: ./chapters/
- reading list: none

## Sources for chapter builds
- notes: ./notes/my_course_notes.md — Alex's consolidated notes from two paid courses; the chapter spine comes from here
- vendor MCPs: none
- web: always, for rot-prone facts only

## Course shape
- chapters: 24 core + 3 optional end sessions (behavioural / story labs)
- behavioural questions: optional sessions only — never mixed into technical drill blocks

## Diagnosed misses
<!-- Dimensions the learner reliably fails (C Completeness · E Evidence · F Framing · D Decision & cost · S Structure). A 0 on any of these caps a drill answer at 5/10. Leave empty until two cycles of data exist. -->
- E — Evidence: knows the numbers, never says them out loud in the answer
- D — Decision & cost: ends on an opinion instead of a costed proposal

## Drill pass threshold
- pass threshold: 5   <!-- score needed for ✅; below it the question stays 📖 and can be drilled again. Set 0 to mark every drilled question ✅ regardless of score. -->

## Embargoes & scope
<!-- Things the skill must honour without being told each session. -->
- "Ledger Copilot" (Alex's side project) — describe the build and the design; never quote adoption or accuracy figures until a verified-numbers card exists
- Investing / markets content is out of scope
- Live-coding rounds are out of scope unless a recruiter confirms one

## Do not nudge
<!-- Decisions the learner has reserved for themselves. -->
- Mock interviews and paid prep platforms — Alex will say when

## Bank conventions
- strong drill answers (≥ 8/10) are appended under the question as a `✔ model answer (D Mon YYYY)` block

## Stale-fact traps
<!-- Facts that were wrong once and will tempt you again. Grows over time — the skill offers to add a line whenever it catches one. -->
- "GPT-4 has an 8k context window" — retired; check the current model card before quoting any context size
- Any LLM-as-judge bias figure from 2023 papers — cite it with its vintage, the numbers have moved
