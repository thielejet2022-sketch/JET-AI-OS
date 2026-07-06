# Memory and Boot Sequence

## Purpose

Memory is one of the highest-value and highest-risk parts of AI-OS.

This spec defines how AI memory, chat context, GitHub specs, connector data, and workflow boot sequences should interact. The goal is to make each session start from the right operating context without relying blindly on any single AI product's memory system.

## Core Problem

Different AI systems handle memory differently.

Some have persistent memory. Some have project instructions. Some rely only on the active chat. Some can read files. Some can access connectors. Some cannot.

If AI-OS depends on hidden memory alone, workflows become fragile and hard to audit. If AI-OS ignores memory entirely, every session becomes repetitive and slow.

The solution is a documented boot sequence that treats GitHub specs as durable memory and product memory as helpful but secondary context.

## Memory Types

### 1. Durable Memory

Durable memory lives in GitHub specs, prompts, decisions, and changelog files.

This is the preferred source for repeatable workflows.

### 2. Product Memory

Product memory is remembered context inside a specific AI platform, such as ChatGPT memory or Claude project context.

This is helpful but may be incomplete, stale, unavailable, or different across platforms.

### 3. Session Memory

Session memory is the current conversation context.

It is useful for immediate continuity but should not be treated as durable unless promoted into GitHub or another declared source of truth.

### 4. Connector Memory

Connector memory is information retrieved from tools such as GitHub, Notion, Airtable, Gmail, Google Calendar, Google Drive, or other systems.

It should be treated according to the source-of-truth ownership model.

### 5. User-Stated Memory

User-stated memory is direct instruction from JET in the current session.

It can override the current run when explicit, but durable changes should be captured in GitHub when they affect future behavior.

## Boot Sequence Goals

A boot sequence should help the acting AI answer:

1. Who is JET?
2. What workflow is being run?
3. What spec controls this workflow?
4. Which systems are available?
5. Which source of truth wins?
6. What constraints must be obeyed?
7. What output should be produced?
8. What should be captured as a durable update?

## Standard Boot Sequence

For any recurring workflow, the AI should proceed as follows:

### Step 1: Identify the Active Workflow

Determine whether the request maps to an existing workflow such as Project Phoenix, Gardening System, Connector Rules, or Automation Watchtower.

If no workflow exists, proceed normally and consider whether a new spec should be created.

### Step 2: Load Durable Specs

Use GitHub or the available source system to read the relevant spec files when possible.

If the specs cannot be accessed, state that limitation and continue using the best available context.

### Step 3: Check Adapter Context

Identify the current AI system, available tools, connector access, and limitations.

Use the LLM compatibility and adapter strategy to decide whether the workflow can run normally or must degrade gracefully.

### Step 4: Resolve Source of Truth

Use the source-of-truth ownership model to identify which system owns the relevant rules, records, documents, or artifacts.

Do not let chat memory override a GitHub spec unless JET explicitly instructs a change.

### Step 5: Apply User Preferences

Apply known durable preferences and current-session instructions.

If there is a conflict, prefer the source-of-truth model and call out the conflict when material.

### Step 6: Execute the Workflow

Produce the required output using the controlling spec.

Use progress/status updates for multi-step work when appropriate.

### Step 7: Capture Drift

If the user corrects the workflow, adds a durable rule, or changes standards, offer to update the relevant GitHub spec or decision file.

### Step 8: Close the Loop

Summarize what was done, what source was used, and what should be updated next.

## Memory Precedence

When memory sources conflict, use this precedence:

1. Current explicit user instruction
2. Workflow-specific GitHub spec
3. GitHub decision file
4. Source-of-truth ownership model
5. Current connector data from the owning system
6. Product memory
7. Session memory
8. AI inference

Current explicit user instruction can direct the current run, but durable future behavior should still be written into GitHub.

## Promotion to Durable Memory

An instruction should be promoted to durable memory when it:

- Changes how a recurring workflow should behave
- Fixes a repeated failure
- Defines a source-of-truth rule
- Adds a connector rule
- Creates a reusable prompt
- Changes formatting standards
- Changes project architecture
- Defines a quality gate

The preferred durable target is GitHub.

## What Not to Store as Durable Memory

Do not automatically promote:

- One-off preferences
- Temporary instructions
- Sensitive personal details unless needed and approved
- Draft wording that is not intended for reuse
- Raw private conversation content
- Guesswork or inferred preferences

## Boot Failure Modes

### Missing Spec

Continue with best effort and suggest creating the spec.

### Missing Connector

State what cannot be accessed and provide manual steps or a degraded output.

### Conflicting Sources

Apply the source-of-truth model and surface the conflict.

### Stale Product Memory

Prefer GitHub and current connector data over remembered context.

### Unknown Model Version

Proceed but mark model/version as unavailable.

## Design Principle

Memory should accelerate execution, not become hidden governance.

The durable rules live where JET can inspect and edit them. AI memory helps carry the backpack, but GitHub holds the map.
