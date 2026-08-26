# AI PM Course — Config

<!--
Your settings. The skill reads this at the start of every session and never edits it without asking.
Fill in the < > bits and delete this comment. Everything else already points at the shipped course.

Keep this file to yourself if you put anything sensitive in the embargo section — it is the only
place personal details live. If you fork this repo publicly, consider adding it to .gitignore.
-->

## Learner
- name: <your first name>
- current role: <role, company type>
- target: <role level · kind of companies · interview timing if known>
- cycle length: 45 min
- delta check cadence: on request only ("delta check" / "bank updated")

## Files
<!-- Relative to the folder this config sits in. -->
- tracker: ./tracker.md
- ledger: ./ledger.md
- bank: ./bank.md
- chapters folder: ./chapters/
- reading list: none

## Sources for chapter builds
<!-- If you have your own course notes, point at them and the chapter spine comes from there.
     With none, chapters are built from the web and general knowledge — that works, it just
     leans harder on the freshness pass. -->
- notes: none
- vendor MCPs: none
- web: always, for rot-prone facts only

## Course shape
- chapters: 34 core + 3 optional end sessions
- behavioural questions: optional sessions only — never mixed into technical drill blocks

## Diagnosed misses
<!--
Dimensions you reliably fail (C Completeness · E Evidence · F Framing · D Decision & cost ·
S Structure). A 0 on any listed dimension caps a drill answer at 5/10 — the gate that stops
you scoring well on an answer that shows the exact habit you're training out.

Leave this empty for now. After two cycles the course will look at your dimension scores and
propose one to three, which is more accurate than guessing on day one.
-->
-

## Drill pass threshold
- pass threshold: 5   <!-- score needed for ✅; below it a question stays 📖 and comes back -->

## Embargoes & scope
<!-- Things the course must honour without being reminded each session. Examples:
     - "<side project>" — describe the build, never quote adoption or accuracy figures
     - <topic> is out of scope -->
-

## Do not nudge
<!-- Decisions you have reserved for yourself. Example:
     - Mock interviews and paid prep platforms — I'll say when -->
-

## Bank conventions
- strong drill answers (≥ 8/10) are appended under the question as a `✔ model answer (D Mon YYYY)` block

## Stale-fact traps
<!-- Facts that were wrong once and will tempt the model again. This list grows as you go:
     whenever a stale fact gets caught, the course offers to add a line here. Examples:
     - Any context-window or pricing number quoted from memory — check the current model card
     - LLM-as-judge bias figures from 2023 papers — cite them with their vintage -->
-
