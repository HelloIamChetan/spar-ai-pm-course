# Grading rubric

Two instruments per cycle: the **MCQ quiz** (scored X/N) and the **drill block** (each answer scored /10 on five dimensions). Both produce numbers that go into the cycle log so the learner can see a trend, not just a feeling.

## MCQ quiz

**Shape:** 5–10 questions. Each is a scenario (2–4 lines), four options of which at least two are plausible traps, one best answer. Number them, present them all in one message, and wait.

**Applied judgment, never recall.** "Which do you do first, given these constraints?" — not "what does RAG stand for?". Draw scenarios from the chapter's §4 decision rules and §9 traps.

**Trap types** (mix them; name the type when scoring a miss):

| Type | The question hides… |
|---|---|
| Premise | a wrong assumption the learner should reject |
| Scale | an answer that's right at 1k users and wrong at 10M |
| Metric | a proxy that looks like the outcome |
| Sequence | the right action in the wrong order |
| Currency | a stale fact (retired model, old price, superseded practice) |
| Cost | the option that's correct but unaffordable or slow |

**Scoring:** `Quiz: 7/9`. For every miss, one line: the trap type and the tell that should have flagged it. For hits, nothing — the learner's time is the scarce resource.

## Drill block

### Dimensions (0–2 each, total /10)

| Dim | 0 | 1 | 2 |
|---|---|---|---|
| **C** Completeness | a part of the question unanswered, or drifted to a different question | every part touched, one thin | every part answered at the depth asked |
| **E** Evidence | no dated fact, number, incident or study | a generic reference ("studies show", "many teams find") | ≥ 1 specific, dated, deployable item — from the chapter's Evidence Bank or the learner's own experience |
| **F** Framing | accepted the premise as stated — no baseline, no "compared to what", no condition under which the answer flips | named one assumption, constraint or condition, then answered as asked (decomposing the problem is structure, not framing) | challenged or clarified the premise first: compared to what, at what volume, what's the baseline, what would change the answer |
| **D** Decision & cost | an opinion, or a list of options | a recommendation without cost, time or owner | a costed proposal: what, how long, what it costs, what we'd learn, the next step — "two days, not two months" |
| **S** Structure | rambling, no shape | shape present but buried | matches the answer shape in the Question map (headline → supports → close); the interviewer could repeat it back |

**Score each dimension against its anchor text first, then add them up.** Never form an overall impression and back-fill the dimensions to match — that is how the same answer scores 4 one week and 7 the next, and the trend line stops meaning anything. When an answer sits between two anchors, the lower one applies unless the answer clearly did the thing the higher anchor describes; an interviewer gives no benefit of the doubt either. Undated evidence is E = 1 however specific the number; a decomposition of the problem is S, not F.

### Gate — diagnosed misses

The config lists the learner's **diagnosed misses**: dimensions they reliably fail. A 0 on any of those caps the answer at **5/10**, whatever the other dimensions earned. Mark it `gate: E` in the score line.

Why non-compensatory: the diagnosed misses are the reason the course exists. An answer that is brilliant on four dimensions and shows the exact habit being trained is, for training purposes, a failed rep — and in the room the interviewer sees the habit, not the brilliance. If the config lists no diagnosed misses yet, there is no gate; after two cycles, propose 1–3 from the lowest dimensions in the cycle log and offer to add them (see `setup.md`).

### Multi-part questions

Hold the learner to every part. If the question asks "how would you evaluate it before launch, and what would you monitor after?", an answer that covers only pre-launch is **C = 0**, not "mostly there". Say which part was dropped. Dropping the second half is one of the most common ways strong candidates lose a round, precisely because the first half felt complete.

### Bands

| Score | Meaning | Bookkeeping |
|---|---|---|
| 9–10 | interview-ready | ✅ in ledger; log the answer into the bank per config's convention |
| 7–8 | solid, one fix | ✅ in ledger; ≥ 8 also goes to the bank |
| 5–6 | mid — the shape is there, the substance isn't | ✅ only if ≥ config's pass threshold (default 5) |
| ≤ 4 | re-drill | stays 📖 in the ledger with the score noted, so it's eligible next block |

### Per-answer format

```
**Q-015 — 4/10** · gate: E
| C | E | F | D | S |
|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 1 |
- Earned: costed the rollout (two-week shadow mode, one engineer) — that's the D=2 shape.
- Lost: never answered the post-launch half (C=0). No evidence deployed (E=0) — the Evidence Bank's <item> was built for exactly this question.
- Say next time: "<one sentence the learner could have said>"
```

Quote what earned points and what lost them. "Good answer, but…" teaches nothing; the quoted phrase and the missing Evidence Bank item do.

### End of block — the biggest gap

Compute the mean per dimension across the block. The biggest gap is the **lowest dimension** (ties → the one that's a diagnosed miss). Name it as: dimension · the question where it cost the most · the one-line fix. Then list anything scored ≤ 4 as "re-drill next cycle".

### Cycle scorecard

Produced in Step 4 and written to the cycle log:

```
Quiz 7/9 · Drilled 4 · Mean 6.5/10 · C/E/F/D/S 1.5/0.8/1.3/1.8/1.3 · gap: E — Q015
Trend (last 3 cycles): E 0.5 → 0.8 → 0.8 → ; D 1.0 → 1.5 → 1.8 ↑
```

The trend comes from the previous cycle-log lines; that's why the log line carries the dimension scores and not just the mean.
