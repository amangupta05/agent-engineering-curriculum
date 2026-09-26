# Chapter briefs

Each brief lists what the chapter must cover. Items marked [added] were not in the original topic list and were added after a gap review. Everything else comes from the original list; verify its version-sensitive claims before writing them.

## Part I. Foundations

**01 What an Agent Is.** The loop of model, tools, and environment. Agents as partially observable sequential decision-making (POMDP framing, state, action, observation) [added]. Workflows vs agents, and when a plain workflow is the better choice. Levels of autonomy: single call, chain, router, tool-using loop, planner-executor, multi-agent. Agent-computer interface (ACI) as a design surface [added]. A decision framework for whether to build an agent at all. Compounding error: per-step reliability to task reliability arithmetic.

**02 Core Patterns and Planning.** ReAct, plan-and-execute, reflection and self-critique (Reflexion), orchestrator-workers, evaluator-optimizer, parallelization (sectioning, voting), routing. Planning and search [added]: Tree of Thoughts, LATS and MCTS over actions, replanning, task decomposition, when search is worth the tokens. Cost and reliability of each pattern.

**03 Tool Calling and Structured Outputs.** JSON Schema tool definitions, parallel tool calls, forced and none tool choice, structured outputs and strict mode, constrained decoding internals (grammar or FSM masking) [added], how each major provider differs (Anthropic, OpenAI, Gemini, open-weight chat templates and tool parsers), validation and repair loops, schema design for reliability.

**04 Reasoning Models Inside Agents.** Extended thinking, interleaved thinking between tool calls, thinking budgets and effort settings, preserving or dropping thinking blocks across turns, cost and latency of reasoning, when a reasoning model helps planning and when it hurts tool loops, test-time compute scaling results.

**05 Harness Engineering.** The code around the model: the loop, stop conditions, retries, max turns, error handling, tool result formatting. System prompt design for agents [added]: role, tool-use guidance, examples, instruction hierarchy. Harness choices that move benchmark scores more than model swaps. Reading and learning from open harnesses (Claude Code, Codex CLI, SWE-agent, OpenHands, mini-SWE-agent) [added].

## Part II. Context, Memory, Retrieval

**06 Context Engineering I: Budget, Caching, Compaction.** The context budget: system prompt, tools, history, retrieved data, scratchpad. Prompt caching: breakpoints, stable prefix, ordering for cache hits, TTLs and cost (worked savings arithmetic per provider). Compaction: triggers, the compaction cliff, validating a summary against the trajectory, compaction as a deliberate choice. Context rot and lost-in-the-middle; why 1M-token windows do not remove curation. Tool result clearing, truncation, pagination of large outputs.

**07 Context Engineering II: Retrieval, Isolation, Progressive Disclosure.** Just-in-time retrieval vs pre-loading; file-system-as-memory; grep and glob tools vs vector RAG. Sub-agents for context isolation. Progressive disclosure: Agent Skills (agentskills.io open standard), lazy tool loading and tool search with hundreds of tools. Note-taking and scratchpads: TODO files, structured progress files for long-horizon tasks. Context engineering for multi-hour runs.

**08 Memory.** Short-term (thread or session) vs long-term. Semantic, episodic, procedural memory. Write policies: what, when, deduplication, conflict resolution, expiry. Tools: Mem0, Zep and Graphiti (temporal knowledge graphs), Letta (MemGPT-style), LangGraph Store, AgentCore Memory, Claude memory tool and Managed Agents memory. Memory as attack surface: memory poisoning, self-poisoning. Multi-tenant isolation. Evaluating memory (LongMemEval, LoCoMo) [added].

**09 Agentic RAG.** Agent decides when and what to retrieve, multi-hop, query rewriting and decomposition. Hybrid search, reranking, GraphRAG, contextual retrieval. Retrieval tools vs pre-injected context, grounding with citations. Deep research agents as the extreme case [added]. Structured data retrieval: text-to-SQL agents, semantic layers [added].

## Part III. Frameworks (each built to the same reference spec: a support agent with 3 tools, memory, one approval gate, tracing, so they compare)

**10 LangGraph.** StateGraph, reducers, conditional edges, checkpointers (Postgres, Redis, DynamoDB), interrupts for HITL, time travel, subgraphs, Store, LangGraph Platform, streaming modes.

**11 Claude Agent SDK and Managed Agents.** The Claude Code harness as a library, built-in tools (bash, file, web), hooks, permission modes, sub-agents, skills, MCP, sessions. Claude Managed Agents (hosted runtime and containers; verify status and date). Anthropic platform tools: Files API, code execution, web search and fetch.

**12 OpenAI Agents SDK and AgentKit.** Agents, handoffs, guardrails, sessions, tracing, Responses API, hosted tools, Agent Builder, ChatKit, Codex as a harness.

**13 Google ADK and Strands Agents.** ADK: LlmAgent, SequentialAgent, ParallelAgent, LoopAgent, session and state services, callbacks, native A2A, deployment to Agent Engine, Cloud Run, GKE. Strands (AWS): model-driven loop, @tool, swarm, graph, agents-as-tools, Bedrock, deployment to AgentCore.

**14 CrewAI, Microsoft Agent Framework, Pydantic AI.** CrewAI: agents, tasks, crews, flows, sequential vs hierarchical, memory. Microsoft Agent Framework (AutoGen plus Semantic Kernel merger; verify GA status), Azure AI Foundry Agent Service. Pydantic AI: typed agents, dependency injection, DBOS and Temporal durable wrappers.

**15 Other Frameworks and Framework Selection.** LlamaIndex Workflows, smolagents (code agents), Agno, Mastra (TypeScript), DSPy (as program optimization), Vercel AI SDK agents [added]. A selection framework: graph vs model-driven vs role-based, lock-in, observability, durability, TypeScript vs Python, and when to use no framework at all [added].

## Part IV. Protocols

**16 Model Context Protocol.** Host, client, server. Tools, resources, prompts. Client features: sampling, elicitation, roots. Transports: stdio and Streamable HTTP, sessions. Recent additions: async Tasks, URL-mode elicitation, extensions, the MCP Registry (verify each against the current spec revision). Auth: OAuth 2.1, protected resource metadata, Client ID Metadata Documents, audience binding. MCP Apps. Governance under the Linux Foundation Agentic AI Foundation (verify). Tool description design and A/B testing descriptions. Server performance and connection pooling [added].

**17 A2A and the Wider Protocol Stack.** A2A (verify v1.0 date and governance), Agent Cards and signed cards, task lifecycle, streaming and push, artifacts, SDKs; A2A vs MCP. AG-UI events. A2UI. Agentic commerce: AP2, ACP, UCP, x402 and the layer each covers. AGENTS.md and the Skills standard as repo conventions. A layered map of the whole stack.

## Part V. Models and Platforms

**18 Model Access Layer and Gateways.** LiteLLM: proxy, virtual keys, budgets, fallbacks, load balancing, cost tracking, Langfuse callbacks. Portkey, OpenRouter, Kong AI Gateway, Cloudflare AI Gateway, Bedrock cross-region inference. Routing: cheap vs frontier per step, cascades, RouteLLM-style learned routers. Rate limits, backoff with jitter, circuit breakers, failover. Semantic vs exact vs provider prompt caching.

**19 Cloud Agent Platforms.** AWS Bedrock: models, Converse API, Bedrock Agents classic vs AgentCore; AgentCore Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability (verify limits such as session length); Bedrock Guardrails, Knowledge Bases. Google Vertex AI Agent Engine, Agentspace (verify current naming), ADK deployment. Azure AI Foundry Agent Service. Anthropic Managed Agents. A comparison table and a portability strategy.

**20 Open-Weight Models for Agents [added].** Which open models are good at tool use (verify with BFCL and similar at time of writing), chat templates and tool parsers in vLLM, SGLang, llama.cpp, Ollama, structured output backends (xgrammar, outlines), serving agents on an 8 GB RTX 4060 (sizes, quantization, context limits), when self-hosting beats APIs for agents (data residency, cost at volume, latency), small models as routers and sub-agents.

## Part VI. Systems

**21 Multi-Agent Systems.** Supervisor, hierarchical, swarm and handoff, network, blackboard. When multi-agent helps (parallel research, context isolation) and when it hurts (coordination overhead, cost multiplier, error compounding). Message passing vs shared state, agent-as-tool vs handoff. Failure modes: loops, role drift, deadlock, duplicated work, conflicting writes. Failure taxonomies from research (MAST) [added]. Cross-organization agents over A2A.

**22 Durable Execution and Long-Running Agents.** Checkpointing (state between nodes) vs durable execution (journal replay). Temporal, Restate, DBOS, Inngest, Hatchet, Step Functions. Idempotency keys and side-effect deduplication on tool calls. Resume after crash, pause for approval over days, background and scheduled agents, event-driven triggers [added]. Rollback risks, compensation (saga) [added], checkpoint integrity. Determinism constraints on LLM calls inside workflows.

**23 Human-in-the-Loop and Agent UX.** Approval gates by risk tier, interrupts, edit-and-resume, escalation. Streaming UX: tokens, tool progress, partial results. Generative UI: AG-UI, A2UI, CopilotKit, Vercel AI SDK, assistant-ui, Streamlit, Chainlit. Trust calibration and explaining agent actions [added]. Voice agents: OpenAI Realtime, Gemini Live, Pipecat, LiveKit Agents, turn detection, latency budgets.

**24 Tool Design and Execution Environments.** Writing good tools: naming, descriptions, actionable errors, compact results, pagination, consolidating tools. Code-as-action vs JSON tool calls. Sandboxes: E2B, Daytona, Modal, Firecracker, gVisor, Docker; filesystem and egress policies. Computer use and browser agents: Claude computer use, OpenAI CUA, Browser Use, Playwright MCP, Stagehand, reliability limits. Integrations at scale: Composio, Arcade, AgentCore Gateway, MCP registries.

**25 Agent Archetypes in Practice [added].** Coding agents (repo maps, edit formats, test-driven loops, SWE-agent ACI), deep research agents, data-analyst and text-to-SQL agents, customer-support agents with policy adherence, back-office process automation agents, multimodal agents (vision, documents). For each: architecture, tools, evaluation, typical failure modes.

## Part VII. Quality

**26 Agent Evaluation.** Levels: unit, step, trajectory, end-to-end, online. Task success, pass@k vs pass^k with arithmetic, tool-call accuracy, trajectory efficiency, policy adherence. Benchmarks: tau-bench and tau2-bench, Terminal-Bench 2.0, SWE-bench Verified, GAIA, WebArena, OSWorld, BFCL, MCP-Bench (verify versions, and benchmark contamination and saturation) [added]. Simulated users and sim-to-real gap. LLM-as-judge for trajectories: rubrics, calibration. Tooling: Langfuse, LangSmith, Braintrust, Phoenix, promptfoo, DeepEval, Inspect AI, Ragas. CI regression gates, golden sets, bootstrap CIs, paired comparisons, sample size.

**27 Testing Agents as Software [added].** Unit testing tools, mocking the model, record and replay of model responses, deterministic fixtures, property-based and fuzz testing of tool inputs, contract tests for MCP servers, environment snapshots, flakiness management with non-deterministic models, testing pyramid for agents.

**28 Observability.** OpenTelemetry GenAI semantic conventions: invoke_agent, execute_tool, chat spans, token usage attributes, MCP spans (verify status of conventions). Langfuse: traces, sessions, scores, prompts, datasets, cost, OTel ingestion. LangSmith, Phoenix, Datadog LLM Observability, AgentCore Observability, OpenLLMetry, Laminar. What to watch: loops, cost per task, tool error rates, latency per step, cache hit rate, drift. PII redaction in traces. Trace-driven debugging workflow [added].

**29 Security for Agents.** OWASP Top 10 for Agentic Applications (verify date), OWASP MCP Top 10, LLM Top 10. Direct and indirect prompt injection, the lethal trifecta, tool poisoning and rug pulls, MCP supply chain, confused deputy, excessive agency, memory poisoning. Defenses: least privilege, per-user OAuth scopes, allowlisted MCP servers, pinned and signed manifests, sandboxing, output filtering, dual-LLM and CaMeL, egress control. Guardrails: NeMo Guardrails, Llama Guard, Bedrock Guardrails, Lakera, classifiers. Red teaming: garak, PyRIT, promptfoo red team, AgentDojo [added]. Agent identity: workload identity, delegated auth, audit logs.

**30 Safety and Alignment of Autonomous Agents [added].** Reward hacking and specification gaming in agents, sandbagging, deceptive or unsanctioned actions in agentic evaluations, AI control (monitoring untrusted agents, trusted monitors), capability thresholds and responsible scaling style policies, designing blast-radius limits, kill switches, and irreversible-action policies.

## Part VIII. Production

**31 Latency, Cost, and Reliability Engineering.** Latency: streaming, parallel tools, speculative execution, small models for routing, caching for TTFT, fewer turns, precomputed context, pooled MCP connections, per-step SLOs. Cost: tokens per task, cache hit ratio, tiering, batch APIs, budget caps per session and tenant, runaway kill switches, a full cost model worked example. Reliability: max iterations, timeouts, retries, fallback models, graceful degradation, deterministic replay.

**32 Scaling, Deployment, and Versioning.** Stateless workers plus external state, queues, concurrency limits, multi-tenancy (tenant-scoped tools, memory, keys). Containerizing agents, Kubernetes, serverless, AgentCore, Agent Engine, Managed Agents. Versioning prompts, tools, and agents together; prompt registries; config-as-code; eval-gated promotion; canary and shadow deployments.

**33 Governance and Compliance [added as its own chapter].** Audit trails, data residency, the EU AI Act obligations and timelines relevant to agents (verify dates), NIST AI RMF, ISO 42001, sector rules, cost attribution, model and vendor risk management, incident response for agents.

**34 Improving Agents Over Time.** Data flywheel from traces to eval sets and fine-tuning data. Prompt optimization (DSPy, GEPA), automatic tool-description tuning. Fine-tuning for tool use (SFT on trajectories), agentic RL (GRPO on trajectories, RL environments, verifiable rewards), what fits on an RTX 4060 and what needs cloud. Links to the FDE roadmap fine-tuning phase.

**35 Delivering Agents as a Forward Deployed Engineer [added].** Discovery and scoping of agent use cases, ROI and cost models for customers, build vs buy vs platform, deploying into customer environments (VPC, on-prem, air-gapped), integration with legacy systems, rollout and change management, success metrics customers accept, writing the design doc and the executive readout.

**36 Capstones.** Five projects with definitions of done, hour estimates, hardware plan, and evaluation protocol: the same agent in 3 frameworks compared on tau-bench-style evals with CIs; an MCP server with OAuth, Tasks, and an MCP Apps UI behind AgentCore Gateway; a cross-framework multi-agent system over A2A (ADK plus Strands plus LangGraph); a durable agent on Temporal with approval gates; a red-team report against your own agent with fixes. Plus a sequencing plan against the FDE roadmap.
