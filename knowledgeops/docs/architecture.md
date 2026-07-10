# KnowledgeOps System Architecture

## Data Flow

Notion workspace -> Audit Engine -> Raw Snapshot -> Metadata Registry -> Rules / Quality / Scoring -> Google Sheets -> Human Decisions -> Notion improvements

## Components

### Audit Engine
Extracts page identity, hierarchy, timestamps, and source metadata.

### Metadata Registry
Stores normalized governance and audit-derived metadata keyed by Page_ID.

### Rules Engine
Assigns priority, rule identifiers, reasons, and deterministic routing recommendations.

### Quality Engine
Evaluates naming, structure, duplication, freshness, governance, connectivity, and completeness.

### Recommendation Engine
Produces explainable Keep, Move, Merge, Rename, Archive, Delete, Review, or Convert recommendations.

### Scoring Engine
Calculates page, project, governance, structure, and workspace health scores.

### Snapshot Engine
Preserves immutable audit runs and generates diffs and trends.

### AI Engine
Adds semantic similarity, clustering, routing, title suggestions, merge recommendations, and advisory summaries.

## Source-of-Truth Boundaries

- Notion owns authored content and human-assigned metadata.
- GitHub owns architecture, ADRs, specifications, tests, and code.
- Google Sheets owns the current operational workflow and reporting interface.
- Snapshot files own historical audit evidence.
