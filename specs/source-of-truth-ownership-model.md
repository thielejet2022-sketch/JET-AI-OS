# Source-of-Truth Ownership Model

## Purpose

JET-AI-OS must prevent GitHub, Notion, Airtable, chat memory, and other systems from becoming competing versions of the truth.

This spec defines how ownership, conflicts, updates, and reconciliation should work across systems.

## Core Problem

JET uses multiple systems for different jobs:

- GitHub for durable Markdown specs, prompts, decisions, and operating rules
- Notion for structured workspaces, planning pages, and human-friendly project views
- Airtable for operational records, structured data, and database-style workflows
- ChatGPT or other AI memory for lightweight continuity and preference recall
- Google Drive or Docs for files, artifacts, drafts, and documents

Without explicit ownership rules, AI-OS could become another system requiring reconciliation instead of reducing friction.

## Ownership Principle

Every durable object should have one primary source of truth.

Other systems may contain views, copies, working drafts, summaries, or execution artifacts, but they should not silently override the primary source.

## Default Ownership Map

| Object Type | Primary Source of Truth | Secondary Systems | Notes |
|---|---|---|---|
| AI-OS operating rules | GitHub | Chat memory, Notion | GitHub wins when rules conflict |
| Workflow specs | GitHub | Notion, Drive | Specs should be Markdown first |
| Reusable prompts | GitHub | Chat memory, Notion | GitHub prompt files are authoritative |
| Durable decisions | GitHub `/decisions` | Chat memory | Decisions should explain what changed and why |
| Changelog | GitHub `changelog.md` | None | GitHub is authoritative |
| Project dashboards | Notion or Airtable | GitHub summaries | Dashboard system owns current view |
| Structured operational records | Airtable | Notion, GitHub exports | Airtable owns row-level structured data |
| Long-form working pages | Notion | GitHub specs | Notion may be workspace, not master rulebook |
| Resume source files | Google Drive or designated repo path | Chat drafts | Ownership must be declared per workflow |
| Chat preferences | ChatGPT memory plus GitHub rules | GitHub | Critical preferences should be promoted to GitHub |

## Conflict Resolution Rules

When systems disagree, use this order unless a workflow spec says otherwise:

1. Workflow-specific source-of-truth declaration
2. GitHub spec or decision file
3. System that owns the object type in the default ownership map
4. Most recent explicitly approved user instruction
5. Chat memory or assistant recollection
6. AI inference

AI inference should never override a documented source.

## Required Source Declaration

Every major spec should include a section called `Source of Truth`.

That section should declare:

- Primary system
- Secondary systems
- Which fields or sections are authoritative
- How updates should flow
- What to do when conflicts appear

## Reconciliation Behavior

When a conflict is detected, the AI should:

1. Name the conflicting systems.
2. Identify the field or rule in conflict.
3. State which source wins under the ownership model.
4. Ask for approval only when the winning source is unclear or the change is material.
5. Offer to update stale secondary systems when connectors allow it.

## Promotion Rule

A chat instruction becomes durable only when one of the following happens:

- It is committed to GitHub.
- It is added to an approved project instruction file.
- It is written into a workflow spec.
- It is captured as a decision.

Until then, it may guide the current session but should not be treated as permanent architecture.

## Demotion Rule

If a rule is obsolete, it should be changed or retired in GitHub rather than merely contradicted in chat.

Major deprecations should be captured in `/decisions`.

## System Roles

### GitHub

Owns durable operating rules, reusable prompts, workflow specs, decisions, and changelog history.

### Notion

Owns human-friendly workspace views, project pages, planning boards, and working notes when explicitly designated.

### Airtable

Owns structured operational records, normalized data, tables, status tracking, and database-style workflows when explicitly designated.

### Chat Memory

Provides continuity and preference recall. It is useful but not authoritative when a GitHub spec exists.

### Google Drive and Docs

Own documents and artifacts when the workflow declares them as source files or final outputs.

## Design Principle

AI-OS should reduce reconciliation burden, not create it.

One object, one owner. Everything else is a view, draft, output, or cache unless explicitly declared otherwise.
