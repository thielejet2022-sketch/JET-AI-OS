# LLM Compatibility and Adapter Strategy

## Purpose

JET-AI-OS is intended to be AI and LLM agnostic. It should work across ChatGPT, Claude, Gemini, Perplexity, local models, future agents, and other AI systems without locking the operating model to a single vendor or product.

This spec defines how AI-OS should account for model identity, model version, capability differences, connector differences, and behavior changes over time.

## Core Problem

AI models change. Capabilities shift. Connector access differs. Memory behavior varies. A workflow that works in one model or version may fail, partially degrade, or behave differently in another.

Without an explicit compatibility strategy, AI-OS becomes brittle. The goal is to make the system portable, inspectable, and adaptable.

## Required Model Context

Whenever a workflow is executed, the acting AI should capture or infer the following when possible:

- AI platform or product name
- Model family
- Model version or release label, if available
- Date of execution
- Available tools or connectors
- Read/write permissions
- Memory availability
- File access availability
- Web access availability
- Known limitations for the current session

If exact model/version information is not available, the AI should state that explicitly rather than guess.

## Adapter Layer Concept

AI-OS should separate durable workflow intent from model-specific execution behavior.

Durable intent belongs in specs. Examples:

- What the workflow is supposed to accomplish
- Required inputs
- Required outputs
- Formatting rules
- Quality gates
- Source-of-truth hierarchy
- Failure modes

Model-specific execution belongs in adapters. Examples:

- How a specific AI reads GitHub
- How a specific AI handles memory
- How a specific AI accesses Notion or Airtable
- How a specific AI creates files
- How a specific AI performs web research
- How a specific AI handles long-running workflows

## Recommended Structure

```text
/specs
  llm-compatibility-and-adapter-strategy.md
/adapters
  README.md
  chatgpt.md
  claude.md
  gemini.md
  perplexity.md
  local-models.md
```

Adapter files should describe capabilities and limitations, not rewrite the master workflow.

## Compatibility Levels

Each workflow should eventually declare a compatibility level:

### Level 1: Read and Reason

The AI can read the spec and provide guidance, but cannot modify connected systems directly.

### Level 2: Read, Reason, and Draft

The AI can read source material and draft outputs, but final changes must be manually applied by JET.

### Level 3: Connected Execution

The AI can read and write at least one connected system such as GitHub, Notion, Gmail, Google Drive, or Airtable.

### Level 4: Multi-System Orchestration

The AI can coordinate across multiple systems while respecting source-of-truth rules.

### Level 5: Conditional or Scheduled Operation

The AI can perform recurring checks, reminders, summaries, or condition watches through an approved automation mechanism.

## Model Change Handling

When a model release changes behavior, workflows should be reviewed for:

- Formatting drift
- Tool access changes
- Memory behavior changes
- Longer or shorter context windows
- Citation behavior
- File creation behavior
- Reasoning quality changes
- Safety or refusal changes
- Connector read/write behavior

Significant changes should be recorded in `changelog.md` or `/decisions`.

## Runtime Compatibility Check

Before running an important workflow, the AI should answer:

1. Which AI system am I using?
2. What tools and connectors are available in this session?
3. What source files or specs are available?
4. What cannot be accessed or verified?
5. Should this run proceed normally, degrade gracefully, or stop for JET approval?

## Graceful Degradation Rules

If a required capability is missing, the AI should not fake completion.

Instead, it should:

1. State the missing capability.
2. Continue with the highest safe compatibility level.
3. Provide manual steps when direct execution is unavailable.
4. Suggest the connector, file, or permission needed to restore full execution.

## Design Principle

AI-OS should define the operating model. Individual AIs should act as interchangeable execution engines.

The workflow should survive model changes because the rules live in GitHub, not only inside a single model's memory or product behavior.
