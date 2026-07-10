# ADR-002: Page_ID is the immutable identifier

- Status: Accepted
- Date: 2026-07-09

## Context
Titles and hierarchy paths can change between audits.

## Decision
Notion Page_ID is the immutable key for identity and snapshot comparison.

## Alternatives
Title, URL, breadcrumb, or generated row number.

## Consequences
Reliable move and rename detection. Missing or duplicate Page_ID values invalidate a snapshot.