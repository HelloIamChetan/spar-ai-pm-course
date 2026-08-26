# Chapter template

Every chapter uses this shape. The point of a fixed shape is consistency across twenty-plus chapters built in different sessions: the learner should know where the decision rules are and where the Evidence Bank is without hunting, and each chapter should cost them the same 10–15 minutes.

**Word budget: 1,400–2,200 words** (≈ 10–15 minutes at reading speed). Under 1,400 usually means §3 or §4 is thin; over 2,200 usually means §3 became an essay. Tables over prose throughout.

---

```markdown
# Ch N — <title>

> Built <D Mon YYYY> · ~<12> min read · Spine: <notes section(s)> · Library: <n> pieces · Web-verified: <n> claims

## 1. Why it matters in the room
<3–5 lines: what interviewers probe with this topic, the question types it unlocks, what a weak answer sounds like.>

## 2. Core concepts
| Concept | What it is (one line) | The interview-grade one-liner |
|---|---|---|
<≤ 8 rows. The one-liner is what the learner should be able to say cold.>

## 3. How it actually works
<≤ 400 words. Mechanisms, not vibes — sequences, components, where it breaks. Tables or numbered steps over paragraphs. This is the spine from the learner's notes.>

## 4. Decision rules & trade-offs
| Situation | Choose | Because | Watch out |
|---|---|---|---|
<4–8 rows. This is what turns knowledge into judgment; MCQs and drills draw from here.>

## 5. Currency — as of <Month YYYY>
| Claim | Value | Source | Verified |
|---|---|---|---|
<3–8 rows. Only facts that rot AND matter for this chapter's questions: model lineup, pricing, context windows, framework landscape, regulation, named incidents. Each row verified live at build time (link) or marked ⚠ unverified. No general news. Verifying eight claims takes real time; pick the ones the learner will actually be asked about.>

## 6. From the library
<1–2 pieces: Title (link) — the one idea to steal.>

## 7. Evidence Bank
| Item | Date | The fact / number | Deploy when asked about… |
|---|---|---|---|
<2–3 dated, citable items — studies, incidents, launches — chosen to be said out loud in an answer.>

## 8. Question map
| Q-id | Question | Answer shape |
|---|---|---|
<Every ledger question this chapter answers, plus any Delta-queue items for this topic. Answer shape = one line: headline → 2–3 supports → close.>

## 9. Traps
<3–5 bullets: how interviewers catch shallow answers on this topic — the tell, and the fix.>
```

---

## Build checklist — run before saving

- Sections present and numbered **1..N with no gaps**. §6 only exists if a library is configured — when it doesn't, renumber the sections that follow so the chapter runs 1–8. A chapter that jumps from §5 to §7 reads like something went missing.
- §5: every row has a source and a Verified mark or ⚠; the heading carries "as of <Month YYYY>"; nothing in it is general news.
- Config's stale-fact traps checked against §2, §3 and §5.
- §7: at least two items, each dated.
- §8: at least three Q-ids, every one present in the ledger under this chapter (or in the Delta queue).
- Word count inside 1,400–2,200.
- The learner's personal details (config) do not appear in the chapter — chapters are course content, not notes about the learner.

## Notes on the freshness pass

Verify, don't recall. Search for the current state of each rot-prone claim, read the primary source where you can (vendor docs, pricing page, paper, incident post-mortem), and record the value with the date you checked. A claim you can't confirm goes in as ⚠ unverified with the best-known value — that is more useful to the learner than silence, and far more useful than a confident stale number they'll repeat in an interview. When a source contradicts something in the notes or in an earlier chapter, say so in the row.
