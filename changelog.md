# Changelog

All notable changes to JET-AI-OS should be captured here.

## 2026-08-30

### Added

- Added `specs/revops-academy-assessment-scoring-model.md` as the canonical RevOps Academy & Assessment Lab Scoring Model v1.0.
- Established six shared scoring dimensions: reasoning, questioning, evidence use and evidence discipline, prioritization, business judgment, and communication.
- Established required separation of observations, hypotheses, evidence requests, inferences, and recommendations.
- Established **insufficiently observed** as the required status when evidence is inadequate for a defensible judgment.
- Confirmed one unified scoring model across Academy Mode and Assessment Lab Mode, with coaching permitted in Academy Mode and restricted during scored assessment unless explicitly allowed.
- Explicitly deferred any canonical numeric scale, weighting model, proficiency bands, aggregation method, or pass/fail threshold until separately reviewed and approved.

### Governance Notes

JET explicitly approved promotion of the identified RevOps Academy & Assessment Lab scoring-model Candidate to canonical GitHub methodology. Historical assessments must retain the methodology version used at the time of assessment.

## 2026-07-06

### Added

- Created the initial README operating model for JET-AI-OS.
- Added `specs/llm-compatibility-and-adapter-strategy.md` to define how AI-OS remains AI and LLM agnostic across model updates, product differences, connectors, and capability changes.
- Added `specs/source-of-truth-ownership-model.md` to define how GitHub, Notion, Airtable, chat memory, Google Drive, and other systems resolve ownership and conflict.
- Added `specs/memory-and-boot-sequence.md` to define how durable memory, product memory, session memory, connector memory, and boot sequence behavior should interact.

### Architectural Notes

Claude review flagged three important gaps:

1. No versioning or compatibility strategy for changing AI models.
2. Source-of-truth ownership was underspecified across GitHub, Notion, Airtable, and other systems.
3. Memory interaction with boot sequence deserved a dedicated spec.

All three concerns were accepted as valid and promoted into first-class architecture specs.