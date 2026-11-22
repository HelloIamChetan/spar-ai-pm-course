# SPAR

**Structured Practice for AI Roles**

**[Try a sample drill](https://helloiamchetan.github.io/spar-ai-pm-course/)** · **[Install the full skill](QUICKSTART.md)**

## Problem

AI product interview prep can turn into reading answers without finding out where your own reasoning breaks down.

## Decision

I designed a practice loop that teaches a topic, quizzes the learner, grades spoken answers against a fixed rubric, and records feedback to revisit. The 34-chapter curriculum and 243-question bank are built around that loop.

## Proof

The browser walkthrough shows an original scenario, an example answer, illustrative feedback, and the next practice recommendation. The full skill writes practice history to local Markdown files.

## Next

Test whether the same answer receives similar scores across fresh model sessions and how those scores compare with a human reference. See the [grading evaluation plan](docs/grading-eval.md).

## What one cycle looks like

About 45 minutes, four steps:

| Step | What happens |
|---|---|
| **1. Chapter** | The coach writes a 10–15 minute chapter from the topic's questions: core concepts, decision rules, a table of facts it verified on the web *today* (model lineups and prices rot), 2–3 dated pieces of evidence you can cite in a room, and a map of exactly which bank questions this chapter answers. |
| **2. Quiz** | 5–10 scenario questions with plausible traps. Applied judgment, not definitions. Scored, with the trap named on every miss. |
| **3. Drills** | 3–5 bank questions, answered out loud. Each answer is scored 0–2 on five dimensions — Completeness, Evidence, Framing, Decision & cost, Structure — for a mark out of 10, with what earned and what lost the points quoted back at you. |
| **4. Books** | Ledger statuses flip, the tracker row and cycle log are written, and the coach re-reads the files to prove it happened. |

The scoring is the part that makes this different from asking a chatbot to quiz you. The same rubric gives learners a common reference for reviewing changes over time. For example, `course status` can show that your Evidence score has risen across six cycles while your Decision score has stayed flat.

### The rubric

| | 0 | 1 | 2 |
|---|---|---|---|
| **C** Completeness | part of the question unanswered | every part touched, one thin | every part answered at depth |
| **E** Evidence | no dated fact or number | a generic reference ("studies show") | a specific, dated, deployable item |
| **F** Framing | accepted the premise | named an assumption, then answered | challenged the premise first — compared to what, at what volume |
| **D** Decision & cost | an opinion, or a list of options | a recommendation with no cost | a costed proposal: what, how long, what we'd learn |
| **S** Structure | rambling | shape buried | headline → supports → close |

Once you've done a couple of cycles, you list your one to three worst dimensions in your config as **diagnosed misses**. After that, a 0 on any of them caps the answer at 5/10 no matter how good the rest was — because in the room the interviewer sees the habit, not the brilliance.

---

## Quickstart

You need [Claude Code](https://claude.com/claude-code) or Claude with file access (Cowork with a connected folder, or claude.ai with attachments).

```bash
git clone https://github.com/HelloIamChetan/spar-ai-pm-course.git
cd spar-ai-pm-course
```

**1. Install the skill.** Copy it where Claude looks for skills:

```bash
mkdir -p ~/.claude/skills
cp -r skill/ai-pm-course ~/.claude/skills/
```

**2. Fill in your config.** Copy the template — `cp course/config.example.md course/ai-pm-course.config.md` — then open your copy and set your name, target roles and timing. The copy is gitignored, so your job search stays on your machine. Two minutes. Leave *Diagnosed misses* empty — the course proposes them from your own scores after two cycles.

**3. Start.**

```
next chapter
```

That's it. Chapter 1 gets built, you get quizzed, you get drilled, the books get kept.

### Commands

| | |
|---|---|
| `start` · `start day 12` | Open a study sitting — shows the plan, then begins |
| `resume` | Pick up the last unfinished sitting exactly where it stopped |
| `stop` | Close the sitting with a bookmark; safe mid-question |
| `next chapter` · `chapter 12` | A full cycle |
| `build chapter 9, skip the drills` | Chapter only |
| `quiz me on RAG` · `drill me` | One step on its own |
| `course status` | Where you are, with the trend in your dimension scores |
| `delta check` | Re-index the bank after you've added questions |

`start` / `stop` are optional — say `next chapter` and work straight through if you prefer. They exist because a 45-minute cycle rarely survives a working day: `stop` mid-drill-block leaves a bookmark, and `resume` picks up without re-asking anything you've already answered.

---

## Bring your own question bank

The shipped bank is a starting point, not a cage. Two ways to make it yours:

**Add to it.** Edit `course/bank.md`, then say `delta check`. Every new question gets indexed against a home chapter, near-duplicates are proposed as merges rather than silently added, and anything out of scope is marked and left alone. Your coverage record stays intact.

**Replace it.** Delete the contents of `course/` (keep the folder), drop in your own list of questions, and say `set up the course from my question bank`. The coach clusters your questions into chapters sized to fit a 45-minute cycle, proposes the curriculum for your approval, then builds the tracker and ledger.

---

## What's in the repo

```
course/                   your course — these files are the memory
  bank.md                 243 questions, grouped by theme, sources credited
  ledger.md               one row per question: home chapter, status, date drilled, score
  tracker.md              curriculum, session bookmark, delta queue, drill ledger, cycle log
  chapters/               chapters land here as they're built
  config.example.md       the config template — copy it to ai-pm-course.config.md
  ai-pm-course.config.md  your settings — the only file with anything personal (gitignored)
skill/ai-pm-course/       the coach
  SKILL.md                the loop
  README.md               how to use it — commands, config, troubleshooting
  references/             sessions, chapter template, grading rubric, data model, setup
  assets/templates/       blank tracker / ledger / bank / config
  scripts/course_tools.py status · next · sitting · verify · delta (stdlib only)
tools/build_course.py     regenerates bank.md and ledger.md from one source list
```

`bank.md` and `ledger.md` are generated so their question text stays byte-identical — that's what keeps delta checks from re-flagging questions that are already indexed. To change the question set properly, edit `tools/build_course.py` and re-run it:

```bash
python3 tools/build_course.py          # regenerate
python3 tools/build_course.py --check  # CI-friendly: fails if they've drifted
```

Editing `bank.md` by hand is fine too — that's the normal way to add questions. Just use `delta check` afterwards so the ledger catches up.

---

## The curriculum

34 chapters, roughly 25 hours if you do one cycle a day. Ordered by dependency: you need to know how a model works before you can argue about what to measure.

| | Chapters |
|---|---|
| **Foundations** | 1–4 — how an LLM is made · the runtime knobs · hallucination · when *not* to use an LLM |
| **Systems** | 5–11 — RAG end to end · RAG in production · context engineering · tool calling & MCP · agent design · agent safety · orchestration & routing |
| **Evals & metrics** | 12–18 — eval foundations · LLM-as-judge · defining success · metric cases · debugging foundations · diagnosing metric drops · diagnosing quality complaints |
| **Product** | 19–23 — designing AI features · judgment calls · design cases (assistants, high-stakes, growth) |
| **Money** | 24–26 — the cost-latency-quality triangle · model selection · unit economics |
| **Risk** | 27–30 — launch gates & fallbacks · responsible AI & regulation · adversarial & abuse · redlines & capability policy |
| **Strategy** | 31–34 — moats & build-vs-buy · pricing & prioritization · roadmapping · builder mindset |
| **Optional** | S25–S27 — Position & POV, and two Story Labs for the behavioural questions, which need your stories rather than a chapter |

Skipping is fine — reorder the curriculum table in `tracker.md` rather than deleting rows, so the coverage record survives.

---

## Sources & credits

The question bank merges nine published AI PM question lists. Where several asked the same thing, the sharpest phrasing was kept and every source credited. **The sources' own answer guidance and named frameworks are deliberately not reproduced here** — those are their work and worth going to directly:

| Code | Source |
|---|---|
| MK | Malay Krishna — 25 AI PM interview questions |
| PF-10 | Product Faculty — AI PM Reference Card (10 categories) |
| PF-15 | Product Faculty — "15 questions and you're hired" |
| OA | A published OpenAI & Anthropic hiring-process infographic |
| SS | Shubham Sharan — 25 questions that actually get asked |
| AS | Anand Sagar — 8 questions across FAANG / startups / consulting |
| AG-84 | Aakash Gupta — AI PM Interview Questions cheat sheet |
| AG-8 | Aakash Gupta — How to Ace the AI PM Interview |
| AK | Anita K — Technical AI PM Interview Questions |

If you're one of these authors and want your questions handled differently, open an issue and it'll be sorted.

---

## Honest limitations

- **The coach is a model, not an interviewer.** It grades against a written rubric. Scores can vary across model runs, and a human interviewer can ask follow-up questions and observe how you respond. Use it to build the reps, not to replace the real thing.
- **Chapters are generated fresh each time.** Facts that rot get verified on the web at build time and date-stamped; everything else comes from the model. Check anything you plan to say as a number in a room.
- **The bank is a snapshot.** It reflects what was being asked when it was compiled. Add to it as you hear real questions — that's what the delta check is for.
- **Behavioural questions need you.** The optional sessions can structure your stories, but nobody can supply the stories.

---

## Licence

Code and the skill: **MIT** — see [LICENSE](LICENSE).
The question bank and course content in `course/`: **CC BY 4.0** — see [LICENSE-CONTENT](LICENSE-CONTENT), and attribution goes to the nine sources above as well as this repo.

Contributions welcome — especially real questions you were asked, with the company and rough date.
