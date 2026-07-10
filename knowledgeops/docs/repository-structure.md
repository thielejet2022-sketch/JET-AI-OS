# Canonical Repository Structure

```text
knowledgeops/
  README.md
  docs/
    architecture.md
    metadata-schema.md
    engine-specs.md
    repository-structure.md
  adrs/
    README.md
    ADR-001-google-sheets-ui.md
    ADR-002-page-id.md
    ADR-003-metadata-separation.md
    ADR-004-rules-before-automation.md
    ADR-005-github-engineering-truth.md
    ADR-006-notion-operational-docs.md
    ADR-007-human-override.md
    ADR-008-immutable-snapshots.md
    ADR-009-rules-quality-separation.md
    ADR-010-reversible-write-pilots.md
  src/
    audit/
    metadata/
    rules/
    quality/
    recommendations/
    scoring/
    snapshots/
    ai/
  tests/
    fixtures/
    unit/
    integration/
  schemas/
  snapshots/
    raw/
    normalized/
    evaluated/
    decisions/
  templates/
  scripts/
  sample-data/
```

Empty implementation directories should be added when the first code and tests are introduced. Snapshot files should never contain secrets or sensitive page content unless the repository access model explicitly permits it.