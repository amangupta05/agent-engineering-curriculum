# Authoring standard for the agent engineering curriculum

Every chapter is a self-contained Markdown file named `NN-Title-With-Dashes.md` in this folder. The reader is an experienced ML engineer who has built production LLM systems (RAG, text-to-SQL, MCP servers, evals) and is preparing for Forward Deployed Engineer roles. Teach from first principles to production mastery, but do not pad Level 1 with things any LLM engineer knows.

## Structure (exact, the verifier checks it)

1. `# Chapter NN: Title`
2. A blockquote with `**What this chapter covers**:`, `**Prerequisites**:` (chapter numbers), `**Where it is used**:`.
3. `---`
4. `## NN.1 Level 1: Foundations` : the mental model, vocabulary, why it exists.
5. `## NN.2 Level 2: Working knowledge` : how to use it correctly, the mechanics, worked examples.
6. `## NN.3 Level 3: Depth` : internals, trade-offs, failure modes, numbers.
7. `## NN.4 Level 4: Mastery` : production design at scale, the decisions a senior engineer makes, edge cases, what the literature and vendors disagree on.
8. `## NN.5 Subtopic checklist` : a checkbox list covering every subtopic in the chapter brief. Nothing in the brief may be missing.
9. `## NN.6 Common misconceptions` : at least 8, each stated then corrected.
10. `## NN.7 Practice` : at least 8 exercises, mixed conceptual, design, and hands-on (hands-on sized for an RTX 4060 8 GB laptop in WSL2 or free tiers).
11. `## NN.8 How this is tested` : at least 12 interview questions, each in `<details><summary>Question</summary>` with a model answer inside. Close every `<details>`.
12. `## NN.9 Summary` : 8 to 15 bullets.
13. `## NN.10 Further reading` : primary sources (papers, specs, official docs) with a one-line note each.

Target 800 to 1,100 lines. At least 5 Mermaid diagrams (flowchart, sequenceDiagram, stateDiagram-v2, quadrantChart, etc.). Tables for comparisons. Worked examples with real arithmetic (token counts, cache savings, cost per task, pass^k, latency budgets). Short code or config snippets are allowed where they clarify a mechanism (a tool JSON schema, a LangGraph state definition, an MCP message), kept under about 25 lines each; this is a textbook, not a code dump.

## Style

- Short sentences. No em dashes anywhere (use commas, colons, parentheses). No filler openings.
- British or American spelling, but consistent within a chapter.
- State numbers with their source and date. Hedge what is uncertain.

## Currency and accuracy (critical)

This field moves monthly and the current date is late September 2026. For every version-sensitive claim (spec versions, release dates, GA or beta status, pricing, product names, API parameter names, benchmark scores, cache TTLs and prices), verify with WebSearch or WebFetch against official docs, specs, or release notes before writing it. The chapter brief may contain claims from the reader's notes; treat those as leads to verify, not facts. If you cannot verify something, either leave it out or write it with "as of <month year>, check the current docs" and never invent a parameter name, version number, score, or date. Prefer explaining durable mechanisms over listing volatile features. Where a vendor claim is marketing, say so.

## Mermaid rules (GitHub rendering)

- Quote every node label: `A["Label"]`, `B{"Decision?"}`, `C(["Rounded"])`. Edge labels quoted: `-->|"text"|`.
- No `#`, `|`, or unescaped `"` inside labels. `<br/>` for line breaks. No colons in Gantt task names.
- quadrantChart points use `Name: [0.3, 0.7]`.
- Keep diagrams under about 25 nodes.

## Do not

- Leave tool-call markup (`<invoke>`, `<parameter>`) in the file.
- Use anything from Atom11 or any real customer. Examples use synthetic companies.
- Write outside your assigned chapter files.
