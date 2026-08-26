#!/usr/bin/env python3
"""
build_course.py — regenerate course/bank.md and course/ledger.md from one source list.

Both files are generated from QUESTIONS below so their question text is byte-identical.
That matters: the skill's delta check matches ledger rows to bank questions by text, so a
paraphrased ledger would make every future delta check re-flag questions already indexed.

    python tools/build_course.py            # writes course/bank.md and course/ledger.md
    python tools/build_course.py --check     # verifies the files match the source, exit 1 if not

Edit QUESTIONS, re-run, commit. Do not hand-edit the generated files.
Stdlib only.
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "course"

# (chapter, question text, source codes)
# Chapter "—" means out of scope (⛔). "S25".."S27" are the optional end sessions.
SECTIONS = [
    ("1. AI / ML and LLM fundamentals", [
        ("Ch1", "How does an LLM actually work, at a high level?", "AK, PF-10"),
        ("Ch1", "What is next-token prediction?", "AK"),
        ("Ch1", "Explain how transformers work. What is attention?", "AK"),
        ("Ch1", "What is the difference between pre-training and post-training?", "AK"),
        ("Ch1", "What are model weights and when do they change?", "AK"),
        ("Ch1", "Why isn't an LLM a database you query?", "AK"),
        ("Ch2", "What are tokens and why do they matter?", "AK"),
        ("Ch2", "What are embeddings, and why do they matter?", "AK, PF-10"),
        ("Ch2", "What does temperature actually control? What is the difference between temperature 0 and temperature 2?", "AK"),
        ("Ch2", "What is a context window and what happens when you exceed it?", "AK"),
        ("Ch2", "Why do two identical prompts give different answers?", "AK"),
        ("Ch3", "Why do models hallucinate, and what is your move as a PM?", "AK"),
        ("Ch3", "Explain how an LLM hallucinates to a non-technical exec, in under a minute.", "SS, AK"),
        ("Ch3", "Does a longer, sterner prompt fix hallucination? Why not?", "AK"),
        ("Ch3", "What is grounding and how do you measure it?", "AK"),
        ("Ch3", "Can you explain a complex AI concept to a non-technical stakeholder?", "MK"),
        ("Ch4", "LLM or classic ML model for churn prediction? Why?", "AK"),
        ("Ch4", "Why XGBoost over an LLM for tabular prediction?", "AK"),
        ("Ch4", "When do you not use an LLM at all?", "AK"),
        ("Ch4", "When does a problem genuinely need AI, and when is a rule-based solution the better product call?", "SS"),
        ("Ch4", "How do you decide when to use AI vs traditional engineering approaches?", "AG-84"),
        ("Ch4", "What does a hybrid system look like in practice?", "AK"),
        ("Ch4", "What are the four layers of the AI product stack?", "AK"),
    ]),
    ("2. RAG, retrieval and context engineering", [
        ("Ch5", "What is RAG and when would you use it? Explain RAG to a non-technical stakeholder.", "AK, PF-10"),
        ("Ch5", "Walk me through a RAG pipeline end to end.", "AK"),
        ("Ch5", "RAG vs fine-tuning vs prompt engineering vs context — when would you choose each?", "PF-10, SS, AS, AK, AG-8"),
        ("Ch5", "What is a vector database and why do you need one?", "AK"),
        ("Ch5", "What is chunking and why does it matter?", "AK"),
        ("Ch5", "When is RAG overkill?", "AK"),
        ("Ch6", "What are the two failure modes of RAG? How would you know if retrieval is failing?", "AK, PF-10"),
        ("Ch6", "How do you evaluate a RAG system — retrieval vs generation? How do you eval faithfulness vs retrieval quality?", "SS, AK"),
        ("Ch6", "Your RAG system has the right document in context but still answers wrong. Why?", "SS, PF-10"),
        ("Ch6", "How would you handle stale, conflicting, or permissioned documents?", "PF-10, AK"),
        ("Ch6", "How would you improve answer accuracy in a RAG product?", "PF-10"),
        ("Ch6", "How would you design a RAG system for enterprise knowledge search, balancing latency, relevance and cost?", "PF-10, AK"),
        ("Ch7", "What is context engineering vs prompt engineering?", "AK"),
        ("Ch7", "What goes into the context window, and in what priority?", "AK"),
        ("Ch7", "The prompt is the product. How do you write and version it as a spec?", "SS"),
        ("Ch7", "How would you prototype a prompt chain for a multi-step task?", "AK"),
    ]),
    ("3. Tools, agents, MCP and orchestration", [
        ("Ch8", "An AI feature calls a tool. What actually happens — does the model execute the function, and if not, who does?", "AK"),
        ("Ch8", "What is in a tool definition (name, description, schema)? Why is a vague tool description a real bug?", "AK"),
        ("Ch8", "How does tool / function calling work under the hood?", "AK"),
        ("Ch8", "What is MCP and why does it exist? How does MCP compare to building one-off API integrations?", "AK"),
        ("Ch8", "What is the difference between a prompt, a tool, and a skill? Do skills retrain the model — what loads at runtime?", "AK"),
        ("Ch9", "What makes something an agent vs a chatbot?", "AK"),
        ("Ch9", "How would you give an agent memory?", "AK"),
        ("Ch9", "When is an agent the right design choice, and when does it just add failure modes?", "SS"),
        ("Ch9", "How would you design an AI agent for customer support? What tools should it have access to?", "PF-10"),
        ("Ch9", "Should we build AI agents now or wait?", "AG-8"),
        ("Ch9", "How would you measure whether an AI agent outperforms human support?", "AG-84"),
        ("Ch9", "Design a roadmap for an AI agent platform. What do you ship first?", "AG-84"),
        ("Ch10", "How would you prevent an agent from taking unsafe or irreversible actions in production?", "PF-10, SS"),
        ("Ch10", "When should the AI ask for approval?", "PF-15"),
        ("Ch10", "Your agent fails halfway through a task. What now?", "PF-15"),
        ("Ch10", "How would you test an autonomous agent before launch, and monitor its behaviour in production?", "PF-10"),
        ("Ch11", "How would you sequence multiple agents with non-overlapping jobs?", "AK"),
        ("Ch11", "How does LangChain work, and when would you use it? LangChain vs LangGraph — what is the difference?", "AK"),
        ("Ch11", "When is a raw SDK call better than a framework? What are the trade-offs of abstraction layers?", "AK"),
        ("Ch11", "What is model routing and why does it matter? Design a router — what does the classifier need to be?", "AK"),
    ]),
    ("4. Evaluation, metrics, measurement and debugging", [
        ("Ch12", "How would you evaluate whether an AI feature is working, before launch?", "PF-10, AK"),
        ("Ch12", "Whiteboard an evaluation framework from scratch.", "AK"),
        ("Ch12", "How would you build an eval set before launch, with no production data?", "PF-10, SS"),
        ("Ch12", "How do we know it improved?", "PF-15"),
        ("Ch12", "Precision, recall, F1 — explain them to a stakeholder.", "AK"),
        ("Ch12", "What is your testing pyramid for an AI product?", "AK"),
        ("Ch13", "What is LLM-as-judge, when do you trust it, and what are its failure modes?", "AK, SS"),
        ("Ch13", "How do you eval a non-deterministic system? How would you set up an A/B test for non-deterministic AI outputs?", "AK, AG-84"),
        ("Ch13", "How do you define success metrics when there is no single correct answer?", "SS, PF-15"),
        ("Ch13", "Set up an evaluation framework for comparing two LLMs on the same task.", "AG-84"),
        ("Ch14", "What metrics would you use for an AI chatbot?", "PF-10"),
        ("Ch14", "How would you measure this AI feature?", "AS"),
        ("Ch14", "How would you measure hallucination rate? Your AI product has a 2% hallucination rate — is that acceptable?", "PF-10, AG-84"),
        ("Ch14", "How do you connect model quality to business outcomes?", "PF-10"),
        ("Ch14", "How do you measure the success of an AI product post-launch?", "MK, AG-84"),
        ("Ch15", "What is the right north-star metric for ChatGPT? How about for Claude?", "AG-84"),
        ("Ch14", "What is the north-star metric for an AI product?", "PF-15"),
        ("Ch15", "Define success metrics for GitHub Copilot. What is the north star?", "AG-84"),
        ("Ch15", "How would you measure success for Claude Projects?", "AG-8"),
        ("Ch14", "How would you measure adoption and retention for an AI product?", "PF-10"),
        ("Ch15", "How do you measure if an AI meeting summarizer is actually reducing information loss?", "AG-84"),
        ("Ch15", "How would you measure success for OpenAI? What if instrumentation went down?", "OA"),
        ("Ch15", "What topline metric goal would you set for Airbnb?", "OA"),
        ("Ch15", "What role does data play in your decision-making process for AI products?", "MK"),
        ("Ch16", "How do you catch regressions after a model swap?", "AK"),
        ("Ch16", "What is observability for AI products?", "AK"),
        ("Ch16", "How would you design a human-in-the-loop feedback system?", "AK"),
        ("Ch16", "Offline evals passed but users are unhappy. What now?", "AK"),
        ("Ch16", "What would you check first when quality drops?", "AK"),
        ("Ch16", "How do you evaluate an agent when the output is a trace, not a single answer?", "AK"),
        ("Ch17", "ChatGPT interactions are down 10% this week. Debug it.", "AG-84"),
        ("Ch17", "Your recommendation model's CTR is declining quarter over quarter. What is happening?", "AG-84"),
        ("Ch17", "You're PM for a recommendation engine. CTR is up but session depth is down. Diagnose.", "AG-84"),
        ("Ch18", "Users complain AI summaries got worse after a model update. Investigate.", "AG-84"),
        ("Ch18", "Your AI writing assistant's retention dropped from 60% to 45%. What do you do?", "AG-84"),
        ("Ch18", "Your AI coding assistant's acceptance rate dropped from 40% to 25%. What happened?", "AG-84"),
        ("Ch17", "An A/B test shows your AI feature wins on engagement but loses on retention. Ship or kill?", "AG-84"),
        ("Ch17", "You launched AI-powered search: click-through up but task completion down. Why?", "AG-84"),
        ("Ch18", "Users say the AI feels stupid. Where do you look?", "PF-15"),
        ("Ch10", "Your agent has 5 steps at 90% reliability each. What is your actual end-to-end success rate — and what do you do about it?", "AK"),
        ("Ch10", "An agent takes a wrong action once in 1,000 runs. When do you ship it and when don't you?", "AK"),
        ("Ch10", "A stakeholder says \"the model's gotten better, so reliability will sort itself out.\" Respond.", "AK"),
        ("Ch26", "Your CEO asks you to prove AI features are worth the compute cost. Build the case.", "AG-84"),
        ("Ch26", "Estimate the number of ChatGPT users worldwide.", "OA"),
    ]),
    ("5. AI product sense and product design", [
        ("Ch19", "How would you design an AI assistant for a specific user workflow?", "PF-10"),
        ("Ch19", "How would you design an AI feature where the output may be wrong?", "PF-10, SS"),
        ("Ch19", "How would you make users trust an AI recommendation? Build a trust and verification system for AI-generated content.", "PF-10, AG-84"),
        ("Ch19", "What makes an AI product meaningfully different from a normal SaaS product?", "PF-10"),
        ("Ch19", "Design an AI feature for a given product.", "AS, AG-8"),
        ("Ch19", "You're PM for ChatGPT. How do you decide what is a model improvement vs an app feature?", "AG-84"),
        ("Ch20", "Your AI coding assistant has a 40% thumbs-down rate from non-technical users. Fix it.", "AG-84"),
        ("Ch20", "You're PM for an AI notetaking tool. Users love the transcript but never use the summary. Why?", "AG-84"),
        ("Ch20", "Your CEO wants to add AI to every product. How do you decide where it adds value?", "AG-84, SS"),
        ("Ch20", "How do you approach user testing and requirements-gathering for AI products?", "MK"),
        ("Ch20", "How do you handle the integration of AI features into existing products?", "MK"),
        ("Ch20", "How do you balance technical feasibility with user needs in AI product development?", "MK"),
        ("Ch21", "How would you improve ChatGPT, Perplexity, Cursor, or Notion AI?", "PF-10"),
        ("Ch21", "Design an AI feature for Gmail that helps users write better emails.", "AG-84"),
        ("Ch21", "Design an AI feature for WhatsApp that helps small businesses respond.", "AG-84"),
        ("Ch21", "Design an AI shopping assistant that handles vague requests like \"something cozy\".", "AG-84"),
        ("Ch22", "How would you design an AI tutor for high school calculus?", "AG-84"),
        ("Ch22", "Design a content moderation system that balances free speech and safety.", "AG-84"),
        ("Ch22", "How would you design the onboarding flow for a new AI coding assistant?", "AG-84"),
        ("Ch22", "Design the conversation flow for an AI therapist bot. What guardrails?", "AG-84"),
        ("Ch23", "How would you redesign the image generation flow in ChatGPT?", "AG-84"),
        ("Ch23", "Design a better interface for Claude's computer-use mode.", "AG-84"),
        ("Ch22", "How would you design a prompt engineering interface for non-technical users?", "AG-84"),
        ("Ch21", "Design an AI travel agent for someone who has never planned a trip.", "AG-84"),
        ("Ch22", "Design an AI-powered code review interface for GitHub.", "AG-84"),
        ("Ch21", "How would you design an AI assistant for elderly users?", "AG-84"),
        ("Ch22", "Design an AI explainer for non-technical stakeholders to understand model decisions.", "AG-84"),
        ("Ch21", "Design an AI feature that summarises unread messages.", "AK"),
        ("Ch23", "How would you grow usage of AI search in an enterprise setting?", "AG-84"),
        ("Ch23", "How would you increase weekly active users of ChatGPT image creation from 175M to 350M in 3 months?", "AG-84"),
        ("Ch23", "What goal would you set for an AI-only social network that OpenAI is building?", "OA"),
        ("Ch23", "What industry could benefit most from enterprise ChatGPT?", "OA"),
        ("Ch23", "What is your favourite product and how would you improve it?", "OA"),
        ("Ch23", "Design an umbrella for kids.", "OA"),
    ]),
    ("6. Cost, latency, model selection and unit economics", [
        ("Ch24", "How would you balance model accuracy vs latency? Latency vs quality vs cost — how do you trade them off?", "PF-10, AK"),
        ("Ch24", "How would you reduce LLM cost without hurting user experience?", "PF-10"),
        ("Ch24", "When would you use a smaller model instead of a larger model?", "PF-10"),
        ("Ch24", "How would you decide whether to stream, cache, or batch AI outputs?", "PF-10"),
        ("Ch24", "What trade-offs would you make before launching an AI feature at scale?", "PF-10"),
        ("Ch25", "How would you choose between the major frontier models or an open-weights model?", "PF-10, AG-84"),
        ("Ch25", "How do you decide which model to use for a task?", "AK"),
        ("Ch25", "How would you prioritise between a frontier API model and training a custom model?", "AG-84"),
        ("Ch25", "Walk me through an AI feature you shipped and the model choices behind it.", "AK"),
        ("Ch25", "How do you keep latency acceptable when every call hits a frontier model?", "SS"),
        ("Ch24", "The best model is 20 times costlier. Now what?", "PF-15"),
        ("Ch24", "How do you decide whether to invest in reducing hallucinations or improving speed?", "AG-84"),
        ("Ch26", "Walk me through the unit economics of an AI feature at 1M users.", "SS"),
        ("Ch26", "The feature is great but per-query cost makes it unprofitable. What do you do?", "SS, PF-15"),
        ("Ch26", "Estimate the inference cost for 10M users. What is the role of GPUs in your cost structure?", "AK"),
        ("Ch26", "How does routing affect unit economics at millions of calls?", "AK"),
        ("Ch26", "When do you choose RAG vs fine-tuning, economically?", "AG-8"),
    ]),
    ("7. Safety, guardrails, responsible AI and regulation", [
        ("Ch27", "What would you do if the AI gives a confident but wrong answer?", "PF-10"),
        ("Ch27", "The model is 90% accurate. Do you launch?", "PF-15"),
        ("Ch27", "How would you design fallback paths for AI failure?", "PF-10"),
        ("Ch27", "How would you reduce hallucinations? What do you do when it hallucinates?", "PF-10, PF-15, AS"),
        ("Ch27", "How would you handle harmful, biased, or unsafe outputs?", "PF-10"),
        ("Ch27", "How would you decide whether an AI product is safe enough to launch? How do you gate an AI-specific launch-readiness review?", "PF-10, SS"),
        ("Ch27", "How do you handle asymmetric harm, where one bad output costs more than many good ones help?", "SS"),
        ("Ch27", "How do you design for failure — bad tool calls, timeouts?", "AK"),
        ("Ch28", "How do you ensure that your AI models are ethical and unbiased?", "MK"),
        ("Ch28", "What is your experience with regulatory compliance in AI product development?", "MK"),
        ("Ch28", "What does the EU AI Act change about shipping a high-risk AI feature?", "SS"),
        ("Ch28", "How do you approach risk management in AI product development?", "MK"),
        ("Ch29", "Your AI product generates fake reviews at scale. You have 2 weeks. What do you do?", "AG-84"),
        ("Ch28", "A bias audit reveals your AI hiring tool discriminates by zip code. Your response?", "AG-84"),
        ("Ch29", "Your chatbot is being manipulated through prompt injection. Fix it.", "AG-84"),
        ("Ch30", "Build a framework for deciding what capabilities are too dangerous to ship.", "AG-84"),
        ("Ch28", "Your AI model memorised PII from training data. What is your incident response?", "AG-84"),
        ("Ch30", "How do you think about the trade-off between capability and potential for misuse?", "AG-84"),
        ("Ch29", "How do you build a red-teaming program for your AI product?", "AG-84"),
        ("Ch30", "Prioritise between a capability improvement and a safety improvement.", "AG-84"),
        ("Ch29", "Design guardrails for an AI that generates legal documents.", "AG-84"),
        ("Ch29", "Your AI generates correct content that could manipulate public opinion. Ship or hold?", "AG-84"),
        ("Ch29", "Handle a government request to modify your AI's behaviour for their market.", "AG-84"),
        ("Ch30", "Where do you draw the safety redlines?", "AK"),
        ("Ch30", "How do you approach AI safety for a chatbot?", "AG-8"),
    ]),
    ("8. Strategy, moats, build vs buy, pricing and GTM", [
        ("Ch31", "What AI product would you build for this company?", "PF-10"),
        ("Ch31", "How would you create a moat around an AI product when a competitor can call the exact same model you do?", "PF-10, SS, AG-84, PF-15"),
        ("Ch31", "Build or buy AI infrastructure? Build vs buy vs fine-tune — walk me through the call.", "PF-15, AG-84, AK, SS"),
        ("Ch31", "The product gets better with every user. Explain.", "PF-15"),
        ("Ch31", "A major competitor made their model free in all products. You are CPO of a rival. What is your strategy?", "AG-84"),
        ("Ch31", "Present a strategy for taking a research breakthrough into a shipped product.", "AG-84"),
        ("Ch32", "How would you price an AI feature — free, paid, or enterprise-only — when inference costs change every quarter?", "PF-10, AG-84"),
        ("Ch33", "How do you set a roadmap when model capabilities improve faster than you can ship?", "SS, PF-15, AK"),
        ("Ch32", "How do you prioritise features in an AI product roadmap?", "MK"),
        ("Ch32", "How would you prioritise AI investments?", "AS"),
        ("Ch32", "You have 3 AI features to prioritise. How do you decide?", "AG-8"),
        ("Ch33", "Write a PRD for multi-modal capabilities in an existing AI product.", "AG-84"),
        ("Ch33", "Build a 12-month roadmap for a healthcare AI assistant.", "AG-84"),
        ("Ch33", "Where do you see AI product management going in the next 3 years?", "AG-84, MK"),
        ("Ch32", "What strategies do you use to communicate the value of AI products to potential customers?", "MK"),
        ("Ch33", "What challenges have you faced in scaling AI products, and how did you overcome them?", "MK"),
    ]),
    ("9. Behavioural, cross-functional and career", [
        ("S25", "Why do you want to work on AI products?", "PF-10"),
        ("S25", "What AI tools do you use every week?", "PF-10"),
        ("S25", "How do you stay current with AI?", "PF-10, MK"),
        ("S25", "What is one AI product you think is underrated or badly designed?", "PF-10"),
        ("S25", "What keeps you up at night about AI?", "AS"),
        ("S25", "Walk me through your journey into AI PM.", "AG-84"),
        ("S25", "What tools and technologies do you find most effective for managing AI projects?", "MK"),
        ("S25", "Can you describe your experience with agile methodologies in AI product management?", "MK"),
        ("S26", "Tell me about an AI product you have shipped. What was the impact?", "AG-84, AS, OA"),
        ("S26", "Can you describe your experience developing AI-driven products from concept to launch?", "MK, OA"),
        ("S26", "Tell me about when an ML model wasn't performing as expected in production.", "AG-84"),
        ("S26", "How have you handled model drift or degradation in production?", "AG-84"),
        ("S26", "Describe a time you balanced model accuracy with other constraints.", "AG-84"),
        ("S26", "Tell me about an AI feature that didn't perform as you hoped. What did you learn?", "AG-84, PF-10"),
        ("S26", "Tell me about a time you killed or rolled back an AI feature. Why?", "SS, AG-84"),
        ("S26", "Describe a time you decided between shipping quickly and waiting for more data.", "AG-84"),
        ("S26", "How do you prioritise ML projects when there is uncertainty about what will work?", "AG-84"),
        ("S27", "Walk me through a time you worked with ML engineers to improve model performance.", "AG-84"),
        ("S27", "How do you collaborate with data scientists and engineers during product development?", "MK, AS"),
        ("S27", "Tell me about a time you disagreed with an ML engineer about approach.", "AG-84"),
        ("S27", "Tell me about a time you pushed back on ML team timelines.", "AG-84"),
        ("S27", "How have you handled it when the ML team wanted to build something cool but not useful?", "AG-84"),
        ("S27", "How do you set expectations when a demo looks magical but production won't be?", "SS"),
        ("S27", "How do you resolve conflicting stakeholder priorities on an AI initiative?", "SS, MK"),
        ("S27", "How do you ensure cross-functional alignment when working on AI initiatives?", "MK"),
        ("S27", "Engineering says 6 months. The CEO wants 6 weeks. What do you do?", "AG-8"),
    ]),
    ("10. Prototyping and builder mindset", [
        ("Ch34", "Tell me about an AI product or prototype you built.", "PF-10"),
        ("Ch34", "How would you prototype an AI feature in one week?", "PF-10"),
        ("Ch34", "What would you build first to validate this AI product idea?", "PF-10"),
        ("Ch34", "How would you use no-code or AI coding tools to test an MVP?", "PF-10"),
        ("Ch34", "What would you hand off to engineering after validating the prototype?", "PF-10"),
    ]),
    ("11. Asked at named companies", [
        ("Ch3", "OpenAI: Define hallucinations in LLMs.", "AK"),
        ("Ch25", "OpenAI: What do you do with a model that has 10x capability at 10x cost?", "AK"),
        ("Ch27", "Anthropic: How do you handle hallucinations in a deployed AI model?", "AK"),
        ("Ch30", "Anthropic: How would you define a \"redline\" for a model?", "AK"),
        ("Ch34", "Google: What AI agents have you built to be more productive?", "AK"),
        ("Ch11", "Google: Design a high-level system for Gemini responding.", "AK"),
        ("Ch26", "Nvidia: Explain how GPUs are used in deep learning.", "AK"),
        ("Ch6", "Nvidia: Design a RAG system with latency, relevance, and cost trade-offs.", "AK"),
        ("Ch5", "Perplexity: Explain how RAG works.", "AK"),
        ("Ch34", "Glean: Have you built any end-to-end agentic systems?", "AK"),
        ("Ch25", "Microsoft: Explain trade-offs in model selection.", "AK"),
        ("Ch11", "Microsoft: Walk through the system design of an AI experience.", "AK"),
        ("Ch18", "Amazon: When did you go deep into an ML system to diagnose a problem?", "AK"),
        ("Ch12", "Meta: Whiteboard an evaluation framework for an AI feature.", "AK"),
    ]),
    ("12. Live-coding questions from engineering loops", [
        ("—", "Parse all URLs from a list and count matches for a given domain, with follow-ups on asynchronous design and scaling.", "OA"),
        ("—", "Scale a token-generating function to handle 100,000 requests per second.", "OA"),
        ("—", "Implement a simple key-value store with evolving constraints around persistence and compression.", "OA"),
    ]),
]

SECTION_NOTES = {
    "9. Behavioural, cross-functional and career":
        "These need your own stories, not a content chapter — they are drilled in the optional end sessions "
        "(S25 Position & POV, S26–S27 Story Labs) with a different rubric.",
    "11. Asked at named companies":
        "Kept as a separate group so the company attribution survives. Each one also has a home chapter; "
        "they are not repeated in the themed lists above.",
    "12. Live-coding questions from engineering loops":
        "⛔ Out of scope for this course — these are software-engineering loop questions, not PM ones. "
        "Kept for reference; move them in scope only if a recruiter confirms a coding round.",
}

SOURCES = """- **MK** — Malay Krishna, 25 AI PM interview questions
- **PF-10** — Product Faculty, AI PM Reference Card (10 categories)
- **PF-15** — Product Faculty, "15 questions and you're hired" card
- **OA** — a published OpenAI & Anthropic hiring-process infographic
- **SS** — Shubham Sharan, 25 questions that actually get asked
- **AS** — Anand Sagar, 8 questions across FAANG / startups / consulting
- **AG-84** — Aakash Gupta, AI PM Interview Questions cheat sheet
- **AG-8** — Aakash Gupta, How to Ace the AI PM Interview (8 question types)
- **AK** — Anita K, Technical AI PM Interview Questions"""

CHAPTERS = [
    (1, "How an LLM is made — data, pre-training, post-training, weights, why it isn't a database"),
    (2, "The runtime knobs — tokens, context window, temperature, embeddings, why identical prompts differ"),
    (3, "Hallucination — why it happens, grounding, the exec explainer, the PM playbook"),
    (4, "When NOT to use an LLM — classic ML vs LLM, hybrid systems, the four-layer AI product stack"),
    (5, "RAG end to end — when to use it, the pipeline, chunking, embeddings, vector DBs"),
    (6, "RAG in production — failure modes, retrieval vs generation evals, stale and permissioned docs"),
    (7, "Context & prompt engineering — window budget and priority, prompt-as-versioned-spec, prompt chains"),
    (8, "Tool calling & MCP — what actually happens, tool definitions, MCP vs one-off integrations"),
    (9, "Agent design — agent vs chatbot, memory, when agents earn their place, the support-agent case"),
    (10, "Agent safety & reliability — approvals, irreversible actions, failure recovery, compounding reliability"),
    (11, "Orchestration & routing — frameworks vs raw SDK, model routing, multi-agent sequencing"),
    (12, "Eval foundations — whiteboard a framework, eval sets with no production data, golden datasets"),
    (13, "LLM-as-judge & non-determinism — judge failure modes, A/B without a single right answer"),
    (14, "Defining success — north stars, the metric framework, connecting model quality to business outcomes"),
    (15, "Metric cases — north stars for named products, and what to do when instrumentation dies"),
    (16, "Debugging foundations — regressions after a model swap, observability, human-in-the-loop, trace evaluation"),
    (17, "Diagnosing metric drops — engagement, CTR, session depth, task completion"),
    (18, "Diagnosing quality complaints — post-update regressions, falling acceptance, \"it feels stupid\""),
    (19, "Designing AI features — the design structure, designing for wrong outputs, trust & verification"),
    (20, "AI product judgment calls — where AI adds value, integration, feasibility vs user needs"),
    (21, "Design cases — assistants and everyday agents"),
    (22, "Design cases — high-stakes and guardrailed products"),
    (23, "Growth cases & warm-ups — moving a number, and the classic non-AI design question"),
    (24, "The cost-latency-quality triangle — reduction levers, stream/cache/batch, what you trade for what"),
    (25, "Model selection — frontier vs small vs open-weights, routing by task, custom models"),
    (26, "Unit economics & estimation — cost at 1M users, inference estimation, GPUs, routing economics"),
    (27, "Launch gates & fallbacks — the 90%-accurate launch call, asymmetric harm, fallback design"),
    (28, "Responsible AI & regulation — bias, PII, compliance, the EU AI Act, risk management"),
    (29, "Adversarial & abuse — prompt injection, red-teaming, misuse at scale, government pressure"),
    (30, "Redlines & capability policy — what is too dangerous to ship, capability vs safety trade-offs"),
    (31, "Moats & build-vs-buy — defensibility when models commoditise, data flywheels, build/buy/fine-tune"),
    (32, "Pricing & prioritization — pricing AI features, ranking investments, communicating value"),
    (33, "Roadmapping under fast model improvement — what stays constant when capabilities move monthly"),
    (34, "Builder mindset — prototyping in a week, no-code validation, what to hand engineering"),
]

SESSIONS = [
    ("S25", "Position & POV — your take on AI, your tools, your journey"),
    ("S26", "Story Lab I — shipping, outcomes, and things that went wrong"),
    ("S27", "Story Lab II — working with engineers, scientists and stakeholders"),
]


def flat():
    out = []
    for section, items in SECTIONS:
        for chapter, text, sources in items:
            out.append((section, chapter, text, sources))
    return out


def build_bank():
    L = ["# Master Question Bank", "",
         "Every distinct question from nine published AI PM question lists, merged and grouped by theme. "
         "Where two or more sources asked the same thing in different words, the sharpest phrasing is kept and "
         "every source is credited. Answer guidance and the sources' own named frameworks are deliberately **not** "
         "reproduced here — go to the originals for those, they are worth your money and attention.", "",
         f"**{len(flat())} questions.** This is your document: add to it, re-word it, cut what doesn't apply. "
         "After you change it, say \"delta check\" and the course will re-index what moved.", "",
         "## Sources", "", SOURCES, "",
         "Strong drill answers get appended under their question as you earn them (see the config's bank convention).", ""]
    for section, items in SECTIONS:
        L += [f"## {section}", ""]
        note = SECTION_NOTES.get(section)
        if note:
            L += [f"*{note}*", ""]
        srcs = sorted({s.strip() for _, _, sr in items for s in sr.split(",")})
        L += [f"*Sources: {', '.join(srcs)}.*", ""]
        for _chapter, text, sources in items:
            L.append(f"- {text} — *{sources}*")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def build_ledger():
    rows = flat()
    L = ["# Question Index & Coverage Ledger", "",
         f"> Baseline: {len(rows)} questions, one row per Master Question Bank entry, in bank order. "
         "This is the diff target for every delta check — a bank question not listed here is new and gets triaged.", "",
         "> Status: ⬜ not covered · 📖 chapter read (or drilled below the pass threshold) · ✅ drilled to standard · "
         "🆕 new since baseline · ⛔ out of scope", "",
         "> Generated by `tools/build_course.py` — the question text matches `bank.md` exactly, which is what makes "
         "delta checks clean. Statuses are yours to change; the text is not.", "",
         "| Q-id | Question | Home ch | Status | Drilled | Score |", "|---|---|---|---|---|---|"]
    for i, (_section, chapter, text, _sources) in enumerate(rows, start=1):
        status = "⛔" if chapter == "—" else "⬜"
        cell = text.replace("|", "\\|")
        L.append(f"| Q{i:03d} | {cell} | {chapter} | {status} |  |  |")
    return "\n".join(L) + "\n"


def build_tracker():
    rows = flat()
    counts = {}
    for _s, ch, _t, _sr in rows:
        counts[ch] = counts.get(ch, 0) + 1
    L = ["# AI PM Course — Tracker", "",
         "> Source of truth for where you are in the course. Personal settings live in `ai-pm-course.config.md`.", "",
         "## Curriculum", "",
         "| # | Chapter | Questions | Status |", "|---|---|---|---|"]
    for n, title in CHAPTERS:
        L.append(f"| {n} | {title} | {counts.get(f'Ch{n}', 0)} | ⬜ |")
    L.append("")
    L += ["*Optional end sessions — behavioural and positioning questions. They need your own stories, "
          "so they are drilled differently and do not gate the technical chapters.*", "",
          "| # | Session | Questions | Status |", "|---|---|---|---|"]
    for code, title in SESSIONS:
        L.append(f"| {code} | {title} | {counts.get(code, 0)} | ⬜ |")
    L += ["",
          "## Standing rules", "",
          "- The config overrides defaults. Embargoes, scope and do-not-nudge items live there.",
          "- Ask twice before deleting anything. Never restructure or delete from the bank without an OK.",
          "- Never guess a rot-prone fact; date-stamp what was verified.",
          "- Never re-ask a ✅ question.", "",
          "## Delta queue", "",
          "*New questions on already-covered topics, waiting to be drilled first in the next block.*", "",
          "| Added | Q-id | Question | Source | Drilled |", "|---|---|---|---|---|", "",
          "## Delta checks", "",
          "*One row per delta check, counting only that check. Merges still awaiting an OK go in Notes.*", "",
          "| Date | +new | merged | queued | ⛔ | Notes |", "|---|---|---|---|---|---|", "",
          "## Drill ledger", "",
          "| Date | Ch | Q-id | Score | Gate | Note |", "|---|---|---|---|---|---|", "",
          "## Cycle log", "",
          "| Date | Ch | Quiz | Drilled | Mean | C/E/F/D/S | Biggest gap |", "|---|---|---|---|---|---|---|", ""]
    return "\n".join(L)


TARGETS = {"bank.md": build_bank, "ledger.md": build_ledger, "tracker.md": build_tracker}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="verify files match the source instead of writing")
    a = ap.parse_args()

    rows = flat()
    ids = {f"Ch{n}" for n, _ in CHAPTERS} | {c for c, _ in SESSIONS} | {"—"}
    bad = sorted({c for _s, c, _t, _sr in rows if c not in ids})
    if bad:
        sys.exit(f"unknown chapter ids in QUESTIONS: {bad}")
    seen, dupes = set(), []
    for _s, _c, t, _sr in rows:
        k = t.lower().strip()
        if k in seen:
            dupes.append(t)
        seen.add(k)
    if dupes:
        sys.exit(f"duplicate question text: {dupes}")

    failed = False
    for name, fn in TARGETS.items():
        content, path = fn(), COURSE / name
        if a.check:
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            # the tracker's statuses are meant to change; only its curriculum is generated
            if name == "tracker.md":
                continue
            if current != content:
                print(f"OUT OF DATE: {name}")
                failed = True
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")

    if a.check:
        print("bank.md and ledger.md match the source" if not failed else "run: python tools/build_course.py")
        sys.exit(1 if failed else 0)

    print(f"\n{len(rows)} questions · "
          f"{sum(1 for _s, c, _t, _sr in rows if c.startswith('Ch'))} in chapters · "
          f"{sum(1 for _s, c, _t, _sr in rows if c.startswith('S'))} in optional sessions · "
          f"{sum(1 for _s, c, _t, _sr in rows if c == '—')} out of scope")


if __name__ == "__main__":
    main()
