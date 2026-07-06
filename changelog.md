# Changelog

All notable changes to JET-AI-OS should be captured here.

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
