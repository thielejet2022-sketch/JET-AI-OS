# JET-AI-OS

JET-AI-OS is the version-controlled operating manual for JET's AI-assisted workflows, project specifications, reusable prompts, connector rules, automation patterns, memory strategy, adapter rules, and decision history.

This repository exists to make AI collaboration more consistent, durable, and repeatable across work, personal projects, research, execution systems, and future AI-enabled tools.

JET-AI-OS is intended to be AI and LLM agnostic. It should define the operating model independently of any single AI vendor, model, release, or product interface.

In plain English: this is the source of truth for how JET and AI systems work together.

## Purpose

Conversational memory is useful, but it is not enough for serious, repeatable workflows. JET-AI-OS turns recurring decisions, standards, prompts, project rules, and operating procedures into durable Markdown files that can be reviewed, versioned, improved, and reused.

The goal is to prevent the same issues from being solved repeatedly in conversation. When a workflow rule matters, it should be captured here.

## What This Project Is

JET-AI-OS is part:

- AI instruction library
- Workflow manual
- Prompt archive
- Project specification system
- Connector rules guide
- Automation design hub
- Memory and boot strategy
- LLM compatibility layer
- Decision log
- Knowledge-base scaffold

It is designed to answer one core question:

> How does JET want AI systems to think, act, document, and execute across his life and work?

## What This Project Is Not

JET-AI-OS is not a random prompt dump, a second Notion workspace, or a full software application by default.

It is the blueprint room for JET's AI operating model. Code may be added later where useful, but the first priority is clear, reusable, human-readable operating documentation.

## Core Principles

The following principles guide this repository:

1. **Durable over disposable**  
   Important instructions should be stored in version-controlled Markdown, not buried in old chats.

2. **Repeatable over improvised**  
   Recurring workflows should have specs, inputs, outputs, failure modes, and restart prompts.

3. **Practical over theoretical**  
   Files should help JET and AI systems execute real work more reliably.

4. **Human-readable first**  
   Markdown should be clear enough for JET to inspect and edit directly.

5. **Connector-aware**  
   Workflows should define which systems are involved, what each connector can do, and where source-of-truth data lives.

6. **Decision-backed**  
   Durable changes should be captured with a short explanation of what changed and why.

7. **No black boxes**  
   AI workflow behavior should be visible, documented, and adjustable.

8. **AI-agnostic by design**  
   Workflow intent should live in specs. Model-specific execution should live in adapters or tool-specific notes.

9. **One object, one owner**  
   GitHub, Notion, Airtable, Drive, and chat memory should not silently compete as equal sources of truth.

10. **Memory is helpful, not sovereign**  
    Product memory can guide a session, but durable rules should live in inspectable files.

## Initial Repository Structure

The planned structure is:

```text
README.md
changelog.md
/specs
  project-phoenix.md
  gardening-system.md
  connector-rules.md
  automation-watchtower.md
  llm-compatibility-and-adapter-strategy.md
  source-of-truth-ownership-model.md
  memory-and-boot-sequence.md
/adapters
  README.md
  chatgpt.md
  claude.md
  gemini.md
  perplexity.md
  local-models.md
/prompts
  README.md
  run-phoenix.md
  final-phoenix.md
  gardening-photo-analysis.md
/decisions
  README.md
```

## Key Architecture Specs

### LLM Compatibility and Adapter Strategy

Defines how AI-OS remains portable across ChatGPT, Claude, Gemini, Perplexity, local models, and future AI systems.

This spec separates durable workflow intent from model-specific execution behavior.

### Source-of-Truth Ownership Model

Defines which system owns which type of information and what happens when GitHub, Notion, Airtable, Drive, chat memory, or other systems disagree.

The default rule is simple: one object, one owner. Everything else is a view, draft, output, or cache unless explicitly declared otherwise.

### Memory and Boot Sequence

Defines how durable memory, product memory, session memory, connector memory, and user-stated instructions interact at the start of a workflow.

The goal is to make each AI session boot from the right operating context without relying blindly on hidden memory.

## Key Workflow Areas

### Project Phoenix

Project Phoenix is JET's job-search and resume-production workflow. It should operate as a practical build system for role-specific application packages, including opportunity intelligence, resume tailoring, ATS alignment, outreach assets, and employer research.

The Phoenix spec should capture required behavior, formatting rules, failure checks, and source-of-truth standards.

### Gardening System

The gardening system documents JET's gardening workflows, including seed tracking, planting status, photo analysis, raised-bed planning, pest observations, and Notion or GitHub organization rules.

The goal is to make gardening observations structured, searchable, and reusable over time.

### Connector Rules

Connector rules define how AI systems should interact with GitHub, Notion, Google Drive, Gmail, Google Calendar, Airtable, and other tools.

This section should reduce confusion about what can be read, edited, searched, created, or treated as source-of-truth.

### Automation Watchtower

The automation watchtower documents reminder patterns, recurring summaries, condition watches, monitoring logic, trigger criteria, and status-board concepts.

The goal is to make future-facing AI work more explicit and reliable.

## How AI Systems Should Use This Repository

When working with JET on a recurring workflow, the acting AI should:

1. Identify the active workflow.
2. Check whether a relevant spec exists.
3. Treat the spec as the preferred source of truth.
4. Check current model, tool, connector, and memory availability.
5. Resolve source-of-truth ownership before updating or reconciling systems.
6. Follow documented workflow rules before improvising.
7. Suggest updates when the workflow changes.
8. Capture durable decisions in Markdown when appropriate.
9. Avoid relying only on product memory for repeatable systems.

## Change Management

Changes to this repo should be made intentionally.

Use `changelog.md` for general updates and `/decisions` for important design choices, workflow shifts, or standards that should persist.

Each meaningful change should answer:

- What changed?
- Why did it change?
- What should AI systems do differently next time?

## Current Status

This repository is in foundation mode.

The first objective is to create a clean structure for JET's AI operating system, then progressively add specs for the highest-value workflows.

## Next Build Steps

Recommended next files:

1. `/adapters/README.md`
2. `/adapters/chatgpt.md`
3. `/adapters/claude.md`
4. `/specs/project-phoenix.md`
5. `/specs/connector-rules.md`
6. `/decisions/README.md`
7. `/prompts/README.md`

## Working Definition

JET-AI-OS is the master operating manual for JET's AI workflows, with GitHub serving as the version-controlled source of truth for specs, prompts, decisions, memory governance, adapter strategy, and reusable project rules.
