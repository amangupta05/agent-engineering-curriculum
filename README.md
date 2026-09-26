# Agent Engineering

A self-contained curriculum on building, evaluating, securing, and operating LLM agents in production, current to September 2026. Thirty-six chapters in eight parts. Each chapter goes from foundations to mastery in four levels, then gives a subtopic checklist, misconceptions, practice, interview questions with model answers, a summary, and primary sources.

`AUTHORING.md` is the chapter standard. `OUTLINE.md` has the full brief for every chapter; items marked [added] came from a gap review of the original topic list. `verify_agents.py` checks structure, style, and Mermaid syntax.

## Chapters

| Part | Chapter |
|---|---|
| I. Foundations | 01 What an Agent Is · 02 Core Patterns and Planning · 03 Tool Calling and Structured Outputs · 04 Reasoning Models Inside Agents · 05 Harness Engineering |
| II. Context, memory, retrieval | 06 Context Engineering I: Budget, Caching, Compaction · 07 Context Engineering II: Retrieval, Isolation, Progressive Disclosure · 08 Memory · 09 Agentic RAG |
| III. Frameworks | 10 LangGraph · 11 Claude Agent SDK and Managed Agents · 12 OpenAI Agents SDK and AgentKit · 13 Google ADK and Strands Agents · 14 CrewAI, Microsoft Agent Framework, Pydantic AI · 15 Other Frameworks and Framework Selection |
| IV. Protocols | 16 Model Context Protocol · 17 A2A and the Wider Protocol Stack |
| V. Models and platforms | 18 Model Access Layer and Gateways · 19 Cloud Agent Platforms · 20 Open-Weight Models for Agents |
| VI. Systems | 21 Multi-Agent Systems · 22 Durable Execution · 23 Human-in-the-Loop and Agent UX · 24 Tool Design and Execution Environments · 25 Agent Archetypes in Practice |
| VII. Quality | 26 Agent Evaluation · 27 Testing Agents as Software · 28 Observability · 29 Security for Agents · 30 Safety and Alignment of Autonomous Agents |
| VIII. Production | 31 Latency, Cost, and Reliability · 32 Scaling, Deployment, and Versioning · 33 Governance and Compliance · 34 Improving Agents Over Time · 35 Delivering Agents as an FDE · 36 Capstones |

## What the gap review added

- Agents as sequential decision-making (POMDP framing) and the agent-computer interface as a design surface.
- Planning and search: Tree of Thoughts, LATS, MCTS over actions, replanning.
- Constrained decoding internals behind structured outputs.
- System prompt design for agents, and reading open harnesses (Claude Code, Codex CLI, SWE-agent, OpenHands).
- Memory benchmarks (LongMemEval, LoCoMo); deep research and text-to-SQL agents as retrieval cases.
- Vercel AI SDK, and when to use no framework.
- Open-weight models for agents: tool parsers, structured output backends, serving on an 8 GB GPU.
- Multi-agent failure taxonomies (MAST); sagas and compensation; event-driven agents.
- Trust calibration in agent UX.
- Agent archetypes: coding, research, data analyst, support, back-office, multimodal.
- Testing agents as software: mocking, record and replay, contract tests, flakiness.
- Benchmark contamination and saturation; AgentDojo for injection testing.
- Safety and alignment of autonomous agents: reward hacking, sandbagging, AI control, blast-radius limits.
- Governance as its own chapter: EU AI Act, NIST AI RMF, ISO 42001.
- Delivering agents as a Forward Deployed Engineer: discovery, ROI, customer environments, readouts.

## Suggested paths

- **Interview in two weeks:** 01, 02, 03, 06, 16, 21, 26, 29, 31, then every "How this is tested" section.
- **Building a production agent now:** 05, 06, 07, 24, 22, 28, 26, 31, 32.
- **Full course alongside the FDE roadmap:** Parts I and II first, one framework chapter (10 or 11) before Part III's others, then Parts IV to VIII in order; chapter 36 maps the capstones onto the roadmap schedule.
