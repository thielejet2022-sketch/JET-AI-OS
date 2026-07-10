# KnowledgeOps Engine Specifications

## Rules Engine

Produces Rule_ID, priority, recommended action, and reason. The first matching priority rule wins. QA checks run separately.

## Quality Engine

Measures naming, structure, duplication, freshness, governance, connectivity, and completeness. A page can have one cleanup priority and multiple quality flags.

## Recommendation Engine

Supports Keep, Move, Merge, Rename, Archive, Delete, Review, and Convert. Recommendations include confidence, evidence, targets, reversibility, and approval requirements.

## Scoring Engine

Calculates page, project, governance, structure, and workspace health. Scores must be explainable and may be capped by critical defects.

## Snapshot Engine

Preserves raw, normalized, evaluated, and decision snapshots. Page_ID is the stable key. Snapshots are timestamped and immutable.

## AI Engine

Supports semantic similarity, clustering, canonical-page suggestions, merge plans, rename suggestions, routing, content-quality review, and weekly advisory summaries. AI cannot execute destructive actions automatically.