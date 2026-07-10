# ADR-008: Every audit run is preserved as an immutable snapshot

- Status: Accepted
- Date: 2026-07-09

## Decision
Every audit run is stored as a timestamped snapshot and is never overwritten.

## Consequences
Reliable diffs, trends, and auditability, with required storage, retention, and validation conventions.