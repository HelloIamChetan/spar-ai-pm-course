# Quickstart

Install once, copy one file, then say `start`.

## 1. Requirements

**Python 3.9+**, already on macOS and most Linux. Nothing to `pip install` — the skill and its
tools are standard library only, and a test fails if that ever changes.

## 2. Install

### Claude Code

```bash
git clone https://github.com/HelloIamChetan/spar-ai-pm-course.git
cd spar-ai-pm-course
mkdir -p ~/.claude/skills
cp -r skill/ai-pm-course ~/.claude/skills/
```

### Claude desktop / web / Cowork

Download `ai-pm-course-<version>.skill` from the
[Releases page](https://github.com/HelloIamChetan/spar-ai-pm-course/releases), attach it to a
conversation, and click **Save skill**.

### Codex

```bash
mkdir -p ~/.agents/skills
cp -r skill/ai-pm-course ~/.agents/skills/
```

### Verify

```bash
python3 ~/.claude/skills/ai-pm-course/scripts/course_tools.py \
  status --tracker course/tracker.md --ledger course/ledger.md
```

Should print `Chapters: 34 total` and `Ledger: 243 questions`.

## 3. Make it yours

```bash
cp course/config.example.md course/ai-pm-course.config.md
```

Open the copy, set your name, target role and timing. **Leave *Diagnosed misses* empty** — the
course proposes them from your own scores after two cycles, which beats guessing on day one.

Your copy is gitignored, so forking this repo and filling it in can't publish your job search.

## 4. Run it

Open Claude in the repo folder and say:

```
start
```

One cycle is about 45 minutes: chapter → quiz → drills → bookkeeping. The commands in short:

| Say | Get |
|---|---|
| `start` · `resume` · `stop` | open, continue or close a study sitting |
| `next chapter` | the next chapter in the curriculum |
| `chapter 12` | that chapter specifically |
| `drill me` · `quiz me on RAG` | just that part of the cycle |
| `course status` | where you are, and whether your scores are moving |
| `delta check` | re-index the ledger after you edit the bank |

Commit `course/` as you go. The tracker becomes an honest record of what you learned.

**Full command reference**, including the read-only scripts and every phrasing the skill
recognises: [`skill/ai-pm-course/QUICKSTART.md`](skill/ai-pm-course/QUICKSTART.md). That copy
ships inside the `.skill` bundle, so it travels with the skill wherever it's installed.

## Troubleshooting

| Symptom | Fix |
|---|---|
| "It didn't find my config." | It looks for `ai-pm-course.config.md` (or any `*course*config*.md`) in the working folder, a `course/` folder, or a connected folder. Did you copy the template, or only edit it in place? |
| Placeholders still in the config | Fine. A `<placeholder>` is a fresh clone, not a broken setup — nothing in a normal cycle needs your name. |
| `course/chapters/` is empty | Intended — see [KNOWN-ISSUES.md](KNOWN-ISSUES.md). Chapters are built when you run a cycle. |
| Delta check flags questions already indexed | The ledger text drifted from the bank. Run `python3 tools/build_course.py --check`. |

Full docs: [README.md](README.md) · [skill/ai-pm-course/README.md](skill/ai-pm-course/README.md)
