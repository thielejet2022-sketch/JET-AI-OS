# ADR-009: Rules and quality checks are separate layers

- Status: Accepted
- Date: 2026-07-09

## Decision
The Rules Engine assigns priority and routing. The Quality Engine measures health and may generate multiple flags.

## Consequences
Clear separation of concerns, with more output fields and coordination between evaluation layers.