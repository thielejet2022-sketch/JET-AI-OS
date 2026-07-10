# ADR-001: Google Sheets is the initial operational UI

- Status: Accepted
- Date: 2026-07-09

## Context
KnowledgeOps needs a fast, inspectable interface for audit metrics, cleanup queues, QA checks, and human decisions.

## Decision
Google Sheets will serve as the initial operational UI.

## Alternatives
- Build a custom web application immediately
- Use Notion as the only interface
- Use CSV files without a dashboard

## Consequences
Fast iteration and transparent formulas, with a planned migration from fragile spreadsheet logic to code-backed processing.