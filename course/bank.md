# Master Question Bank

Every distinct question from nine published AI PM question lists, merged and grouped by theme. Where two or more sources asked the same thing in different words, the sharpest phrasing is kept and every source is credited. Answer guidance and the sources' own named frameworks are deliberately **not** reproduced here — go to the originals for those, they are worth your money and attention.

**243 questions.** This is your document: add to it, re-word it, cut what doesn't apply. After you change it, say "delta check" and the course will re-index what moved.

## Sources

- **MK** — Malay Krishna, 25 AI PM interview questions
- **PF-10** — Product Faculty, AI PM Reference Card (10 categories)
- **PF-15** — Product Faculty, "15 questions and you're hired" card
- **OA** — a published OpenAI & Anthropic hiring-process infographic
- **SS** — Shubham Sharan, 25 questions that actually get asked
- **AS** — Anand Sagar, 8 questions across FAANG / startups / consulting
- **AG-84** — Aakash Gupta, AI PM Interview Questions cheat sheet
- **AG-8** — Aakash Gupta, How to Ace the AI PM Interview (8 question types)
- **AK** — Anita K, Technical AI PM Interview Questions

Strong drill answers get appended under their question as you earn them (see the config's bank convention).

## 1. AI / ML and LLM fundamentals

*Sources: AG-84, AK, MK, PF-10, SS.*

- How does an LLM actually work, at a high level? — *AK, PF-10*
- What is next-token prediction? — *AK*
- Explain how transformers work. What is attention? — *AK*
- What is the difference between pre-training and post-training? — *AK*
- What are model weights and when do they change? — *AK*
- Why isn't an LLM a database you query? — *AK*
- What are tokens and why do they matter? — *AK*
- What are embeddings, and why do they matter? — *AK, PF-10*
- What does temperature actually control? What is the difference between temperature 0 and temperature 2? — *AK*
- What is a context window and what happens when you exceed it? — *AK*
- Why do two identical prompts give different answers? — *AK*
- Why do models hallucinate, and what is your move as a PM? — *AK*
- Explain how an LLM hallucinates to a non-technical exec, in under a minute. — *SS, AK*
- Does a longer, sterner prompt fix hallucination? Why not? — *AK*
- What is grounding and how do you measure it? — *AK*
- Can you explain a complex AI concept to a non-technical stakeholder? — *MK*
- LLM or classic ML model for churn prediction? Why? — *AK*
- Why XGBoost over an LLM for tabular prediction? — *AK*
- When do you not use an LLM at all? — *AK*
- When does a problem genuinely need AI, and when is a rule-based solution the better product call? — *SS*
- How do you decide when to use AI vs traditional engineering approaches? — *AG-84*
- What does a hybrid system look like in practice? — *AK*
- What are the four layers of the AI product stack? — *AK*

## 2. RAG, retrieval and context engineering

*Sources: AG-8, AK, AS, PF-10, SS.*

- What is RAG and when would you use it? Explain RAG to a non-technical stakeholder. — *AK, PF-10*
- Walk me through a RAG pipeline end to end. — *AK*
- RAG vs fine-tuning vs prompt engineering vs context — when would you choose each? — *PF-10, SS, AS, AK, AG-8*
- What is a vector database and why do you need one? — *AK*
- What is chunking and why does it matter? — *AK*
- When is RAG overkill? — *AK*
- What are the two failure modes of RAG? How would you know if retrieval is failing? — *AK, PF-10*
- How do you evaluate a RAG system — retrieval vs generation? How do you eval faithfulness vs retrieval quality? — *SS, AK*
- Your RAG system has the right document in context but still answers wrong. Why? — *SS, PF-10*
- How would you handle stale, conflicting, or permissioned documents? — *PF-10, AK*
- How would you improve answer accuracy in a RAG product? — *PF-10*
- How would you design a RAG system for enterprise knowledge search, balancing latency, relevance and cost? — *PF-10, AK*
- What is context engineering vs prompt engineering? — *AK*
- What goes into the context window, and in what priority? — *AK*
- The prompt is the product. How do you write and version it as a spec? — *SS*
- How would you prototype a prompt chain for a multi-step task? — *AK*

## 3. Tools, agents, MCP and orchestration

*Sources: AG-8, AG-84, AK, PF-10, PF-15, SS.*

- An AI feature calls a tool. What actually happens — does the model execute the function, and if not, who does? — *AK*
- What is in a tool definition (name, description, schema)? Why is a vague tool description a real bug? — *AK*
- How does tool / function calling work under the hood? — *AK*
- What is MCP and why does it exist? How does MCP compare to building one-off API integrations? — *AK*
- What is the difference between a prompt, a tool, and a skill? Do skills retrain the model — what loads at runtime? — *AK*
- What makes something an agent vs a chatbot? — *AK*
- How would you give an agent memory? — *AK*
- When is an agent the right design choice, and when does it just add failure modes? — *SS*
- How would you design an AI agent for customer support? What tools should it have access to? — *PF-10*
- Should we build AI agents now or wait? — *AG-8*
- How would you measure whether an AI agent outperforms human support? — *AG-84*
- Design a roadmap for an AI agent platform. What do you ship first? — *AG-84*
- How would you prevent an agent from taking unsafe or irreversible actions in production? — *PF-10, SS*
- When should the AI ask for approval? — *PF-15*
- Your agent fails halfway through a task. What now? — *PF-15*
- How would you test an autonomous agent before launch, and monitor its behaviour in production? — *PF-10*
- How would you sequence multiple agents with non-overlapping jobs? — *AK*
- How does LangChain work, and when would you use it? LangChain vs LangGraph — what is the difference? — *AK*
- When is a raw SDK call better than a framework? What are the trade-offs of abstraction layers? — *AK*
- What is model routing and why does it matter? Design a router — what does the classifier need to be? — *AK*

## 4. Evaluation, metrics, measurement and debugging

*Sources: AG-8, AG-84, AK, AS, MK, OA, PF-10, PF-15, SS.*

- How would you evaluate whether an AI feature is working, before launch? — *PF-10, AK*
- Whiteboard an evaluation framework from scratch. — *AK*
- How would you build an eval set before launch, with no production data? — *PF-10, SS*
- How do we know it improved? — *PF-15*
- Precision, recall, F1 — explain them to a stakeholder. — *AK*
- What is your testing pyramid for an AI product? — *AK*
- What is LLM-as-judge, when do you trust it, and what are its failure modes? — *AK, SS*
- How do you eval a non-deterministic system? How would you set up an A/B test for non-deterministic AI outputs? — *AK, AG-84*
- How do you define success metrics when there is no single correct answer? — *SS, PF-15*
- Set up an evaluation framework for comparing two LLMs on the same task. — *AG-84*
- What metrics would you use for an AI chatbot? — *PF-10*
- How would you measure this AI feature? — *AS*
- How would you measure hallucination rate? Your AI product has a 2% hallucination rate — is that acceptable? — *PF-10, AG-84*
- How do you connect model quality to business outcomes? — *PF-10*
- How do you measure the success of an AI product post-launch? — *MK, AG-84*
- What is the right north-star metric for ChatGPT? How about for Claude? — *AG-84*
- What is the north-star metric for an AI product? — *PF-15*
- Define success metrics for GitHub Copilot. What is the north star? — *AG-84*
- How would you measure success for Claude Projects? — *AG-8*
- How would you measure adoption and retention for an AI product? — *PF-10*
- How do you measure if an AI meeting summarizer is actually reducing information loss? — *AG-84*
- How would you measure success for OpenAI? What if instrumentation went down? — *OA*
- What topline metric goal would you set for Airbnb? — *OA*
- What role does data play in your decision-making process for AI products? — *MK*
- How do you catch regressions after a model swap? — *AK*
- What is observability for AI products? — *AK*
- How would you design a human-in-the-loop feedback system? — *AK*
- Offline evals passed but users are unhappy. What now? — *AK*
- What would you check first when quality drops? — *AK*
- How do you evaluate an agent when the output is a trace, not a single answer? — *AK*
- ChatGPT interactions are down 10% this week. Debug it. — *AG-84*
- Your recommendation model's CTR is declining quarter over quarter. What is happening? — *AG-84*
- You're PM for a recommendation engine. CTR is up but session depth is down. Diagnose. — *AG-84*
- Users complain AI summaries got worse after a model update. Investigate. — *AG-84*
- Your AI writing assistant's retention dropped from 60% to 45%. What do you do? — *AG-84*
- Your AI coding assistant's acceptance rate dropped from 40% to 25%. What happened? — *AG-84*
- An A/B test shows your AI feature wins on engagement but loses on retention. Ship or kill? — *AG-84*
- You launched AI-powered search: click-through up but task completion down. Why? — *AG-84*
- Users say the AI feels stupid. Where do you look? — *PF-15*
- Your agent has 5 steps at 90% reliability each. What is your actual end-to-end success rate — and what do you do about it? — *AK*
- An agent takes a wrong action once in 1,000 runs. When do you ship it and when don't you? — *AK*
- A stakeholder says "the model's gotten better, so reliability will sort itself out." Respond. — *AK*
- Your CEO asks you to prove AI features are worth the compute cost. Build the case. — *AG-84*
- Estimate the number of ChatGPT users worldwide. — *OA*

## 5. AI product sense and product design

*Sources: AG-8, AG-84, AK, AS, MK, OA, PF-10, SS.*

- How would you design an AI assistant for a specific user workflow? — *PF-10*
- How would you design an AI feature where the output may be wrong? — *PF-10, SS*
- How would you make users trust an AI recommendation? Build a trust and verification system for AI-generated content. — *PF-10, AG-84*
- What makes an AI product meaningfully different from a normal SaaS product? — *PF-10*
- Design an AI feature for a given product. — *AS, AG-8*
- You're PM for ChatGPT. How do you decide what is a model improvement vs an app feature? — *AG-84*
- Your AI coding assistant has a 40% thumbs-down rate from non-technical users. Fix it. — *AG-84*
- You're PM for an AI notetaking tool. Users love the transcript but never use the summary. Why? — *AG-84*
- Your CEO wants to add AI to every product. How do you decide where it adds value? — *AG-84, SS*
- How do you approach user testing and requirements-gathering for AI products? — *MK*
- How do you handle the integration of AI features into existing products? — *MK*
- How do you balance technical feasibility with user needs in AI product development? — *MK*
- How would you improve ChatGPT, Perplexity, Cursor, or Notion AI? — *PF-10*
- Design an AI feature for Gmail that helps users write better emails. — *AG-84*
- Design an AI feature for WhatsApp that helps small businesses respond. — *AG-84*
- Design an AI shopping assistant that handles vague requests like "something cozy". — *AG-84*
- How would you design an AI tutor for high school calculus? — *AG-84*
- Design a content moderation system that balances free speech and safety. — *AG-84*
- How would you design the onboarding flow for a new AI coding assistant? — *AG-84*
- Design the conversation flow for an AI therapist bot. What guardrails? — *AG-84*
- How would you redesign the image generation flow in ChatGPT? — *AG-84*
- Design a better interface for Claude's computer-use mode. — *AG-84*
- How would you design a prompt engineering interface for non-technical users? — *AG-84*
- Design an AI travel agent for someone who has never planned a trip. — *AG-84*
- Design an AI-powered code review interface for GitHub. — *AG-84*
- How would you design an AI assistant for elderly users? — *AG-84*
- Design an AI explainer for non-technical stakeholders to understand model decisions. — *AG-84*
- Design an AI feature that summarises unread messages. — *AK*
- How would you grow usage of AI search in an enterprise setting? — *AG-84*
- How would you increase weekly active users of ChatGPT image creation from 175M to 350M in 3 months? — *AG-84*
- What goal would you set for an AI-only social network that OpenAI is building? — *OA*
- What industry could benefit most from enterprise ChatGPT? — *OA*
- What is your favourite product and how would you improve it? — *OA*
- Design an umbrella for kids. — *OA*

## 6. Cost, latency, model selection and unit economics

*Sources: AG-8, AG-84, AK, PF-10, PF-15, SS.*

- How would you balance model accuracy vs latency? Latency vs quality vs cost — how do you trade them off? — *PF-10, AK*
- How would you reduce LLM cost without hurting user experience? — *PF-10*
- When would you use a smaller model instead of a larger model? — *PF-10*
- How would you decide whether to stream, cache, or batch AI outputs? — *PF-10*
- What trade-offs would you make before launching an AI feature at scale? — *PF-10*
- How would you choose between the major frontier models or an open-weights model? — *PF-10, AG-84*
- How do you decide which model to use for a task? — *AK*
- How would you prioritise between a frontier API model and training a custom model? — *AG-84*
- Walk me through an AI feature you shipped and the model choices behind it. — *AK*
- How do you keep latency acceptable when every call hits a frontier model? — *SS*
- The best model is 20 times costlier. Now what? — *PF-15*
- How do you decide whether to invest in reducing hallucinations or improving speed? — *AG-84*
- Walk me through the unit economics of an AI feature at 1M users. — *SS*
- The feature is great but per-query cost makes it unprofitable. What do you do? — *SS, PF-15*
- Estimate the inference cost for 10M users. What is the role of GPUs in your cost structure? — *AK*
- How does routing affect unit economics at millions of calls? — *AK*
- When do you choose RAG vs fine-tuning, economically? — *AG-8*

## 7. Safety, guardrails, responsible AI and regulation

*Sources: AG-8, AG-84, AK, AS, MK, PF-10, PF-15, SS.*

- What would you do if the AI gives a confident but wrong answer? — *PF-10*
- The model is 90% accurate. Do you launch? — *PF-15*
- How would you design fallback paths for AI failure? — *PF-10*
- How would you reduce hallucinations? What do you do when it hallucinates? — *PF-10, PF-15, AS*
- How would you handle harmful, biased, or unsafe outputs? — *PF-10*
- How would you decide whether an AI product is safe enough to launch? How do you gate an AI-specific launch-readiness review? — *PF-10, SS*
- How do you handle asymmetric harm, where one bad output costs more than many good ones help? — *SS*
- How do you design for failure — bad tool calls, timeouts? — *AK*
- How do you ensure that your AI models are ethical and unbiased? — *MK*
- What is your experience with regulatory compliance in AI product development? — *MK*
- What does the EU AI Act change about shipping a high-risk AI feature? — *SS*
- How do you approach risk management in AI product development? — *MK*
- Your AI product generates fake reviews at scale. You have 2 weeks. What do you do? — *AG-84*
- A bias audit reveals your AI hiring tool discriminates by zip code. Your response? — *AG-84*
- Your chatbot is being manipulated through prompt injection. Fix it. — *AG-84*
- Build a framework for deciding what capabilities are too dangerous to ship. — *AG-84*
- Your AI model memorised PII from training data. What is your incident response? — *AG-84*
- How do you think about the trade-off between capability and potential for misuse? — *AG-84*
- How do you build a red-teaming program for your AI product? — *AG-84*
- Prioritise between a capability improvement and a safety improvement. — *AG-84*
- Design guardrails for an AI that generates legal documents. — *AG-84*
- Your AI generates correct content that could manipulate public opinion. Ship or hold? — *AG-84*
- Handle a government request to modify your AI's behaviour for their market. — *AG-84*
- Where do you draw the safety redlines? — *AK*
- How do you approach AI safety for a chatbot? — *AG-8*

## 8. Strategy, moats, build vs buy, pricing and GTM

*Sources: AG-8, AG-84, AK, AS, MK, PF-10, PF-15, SS.*

- What AI product would you build for this company? — *PF-10*
- How would you create a moat around an AI product when a competitor can call the exact same model you do? — *PF-10, SS, AG-84, PF-15*
- Build or buy AI infrastructure? Build vs buy vs fine-tune — walk me through the call. — *PF-15, AG-84, AK, SS*
- The product gets better with every user. Explain. — *PF-15*
- A major competitor made their model free in all products. You are CPO of a rival. What is your strategy? — *AG-84*
- Present a strategy for taking a research breakthrough into a shipped product. — *AG-84*
- How would you price an AI feature — free, paid, or enterprise-only — when inference costs change every quarter? — *PF-10, AG-84*
- How do you set a roadmap when model capabilities improve faster than you can ship? — *SS, PF-15, AK*
- How do you prioritise features in an AI product roadmap? — *MK*
- How would you prioritise AI investments? — *AS*
- You have 3 AI features to prioritise. How do you decide? — *AG-8*
- Write a PRD for multi-modal capabilities in an existing AI product. — *AG-84*
- Build a 12-month roadmap for a healthcare AI assistant. — *AG-84*
- Where do you see AI product management going in the next 3 years? — *AG-84, MK*
- What strategies do you use to communicate the value of AI products to potential customers? — *MK*
- What challenges have you faced in scaling AI products, and how did you overcome them? — *MK*

## 9. Behavioural, cross-functional and career

*These need your own stories, not a content chapter — they are drilled in the optional end sessions (S25 Position & POV, S26–S27 Story Labs) with a different rubric.*

*Sources: AG-8, AG-84, AS, MK, OA, PF-10, SS.*

- Why do you want to work on AI products? — *PF-10*
- What AI tools do you use every week? — *PF-10*
- How do you stay current with AI? — *PF-10, MK*
- What is one AI product you think is underrated or badly designed? — *PF-10*
- What keeps you up at night about AI? — *AS*
- Walk me through your journey into AI PM. — *AG-84*
- What tools and technologies do you find most effective for managing AI projects? — *MK*
- Can you describe your experience with agile methodologies in AI product management? — *MK*
- Tell me about an AI product you have shipped. What was the impact? — *AG-84, AS, OA*
- Can you describe your experience developing AI-driven products from concept to launch? — *MK, OA*
- Tell me about when an ML model wasn't performing as expected in production. — *AG-84*
- How have you handled model drift or degradation in production? — *AG-84*
- Describe a time you balanced model accuracy with other constraints. — *AG-84*
- Tell me about an AI feature that didn't perform as you hoped. What did you learn? — *AG-84, PF-10*
- Tell me about a time you killed or rolled back an AI feature. Why? — *SS, AG-84*
- Describe a time you decided between shipping quickly and waiting for more data. — *AG-84*
- How do you prioritise ML projects when there is uncertainty about what will work? — *AG-84*
- Walk me through a time you worked with ML engineers to improve model performance. — *AG-84*
- How do you collaborate with data scientists and engineers during product development? — *MK, AS*
- Tell me about a time you disagreed with an ML engineer about approach. — *AG-84*
- Tell me about a time you pushed back on ML team timelines. — *AG-84*
- How have you handled it when the ML team wanted to build something cool but not useful? — *AG-84*
- How do you set expectations when a demo looks magical but production won't be? — *SS*
- How do you resolve conflicting stakeholder priorities on an AI initiative? — *SS, MK*
- How do you ensure cross-functional alignment when working on AI initiatives? — *MK*
- Engineering says 6 months. The CEO wants 6 weeks. What do you do? — *AG-8*

## 10. Prototyping and builder mindset

*Sources: PF-10.*

- Tell me about an AI product or prototype you built. — *PF-10*
- How would you prototype an AI feature in one week? — *PF-10*
- What would you build first to validate this AI product idea? — *PF-10*
- How would you use no-code or AI coding tools to test an MVP? — *PF-10*
- What would you hand off to engineering after validating the prototype? — *PF-10*

## 11. Asked at named companies

*Kept as a separate group so the company attribution survives. Each one also has a home chapter; they are not repeated in the themed lists above.*

*Sources: AK.*

- OpenAI: Define hallucinations in LLMs. — *AK*
- OpenAI: What do you do with a model that has 10x capability at 10x cost? — *AK*
- Anthropic: How do you handle hallucinations in a deployed AI model? — *AK*
- Anthropic: How would you define a "redline" for a model? — *AK*
- Google: What AI agents have you built to be more productive? — *AK*
- Google: Design a high-level system for Gemini responding. — *AK*
- Nvidia: Explain how GPUs are used in deep learning. — *AK*
- Nvidia: Design a RAG system with latency, relevance, and cost trade-offs. — *AK*
- Perplexity: Explain how RAG works. — *AK*
- Glean: Have you built any end-to-end agentic systems? — *AK*
- Microsoft: Explain trade-offs in model selection. — *AK*
- Microsoft: Walk through the system design of an AI experience. — *AK*
- Amazon: When did you go deep into an ML system to diagnose a problem? — *AK*
- Meta: Whiteboard an evaluation framework for an AI feature. — *AK*

## 12. Live-coding questions from engineering loops

*⛔ Out of scope for this course — these are software-engineering loop questions, not PM ones. Kept for reference; move them in scope only if a recruiter confirms a coding round.*

*Sources: OA.*

- Parse all URLs from a list and count matches for a given domain, with follow-ups on asynchronous design and scaling. — *OA*
- Scale a token-generating function to handle 100,000 requests per second. — *OA*
- Implement a simple key-value store with evolving constraints around persistence and compression. — *OA*
