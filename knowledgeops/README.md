# KnowledgeOps

KnowledgeOps is a knowledge-operations platform for making large personal knowledge bases measurable, governed, continuously improving, and increasingly self-organizing through analytics, automation, and AI.

## Platform Roles

- Notion: living operational documentation and human context
- GitHub: engineering architecture, ADRs, specifications, tests, and code
- Google Sheets: operational dashboard, audit queue, QA, and trend reporting

## Architecture

- Audit Engine
- Metadata Registry
- Rules Engine
- Quality Engine
- Recommendation Engine
- Scoring Engine
- Snapshot Engine
- AI Engine

## Current Milestone

Milestone Beta: Snapshot and Rules MVP

## Run the Pipeline

From the `knowledgeops` directory:

```bash
python -m pip install -e ".[dev]"
python -m knowledgeops.cli sample-data/sanitized-audit.csv \
  --output-csv evaluated-snapshot.csv \
  --output-json evaluated-snapshot.json
```

The input CSV matches the current Google Sheet audit headers:

```text
Title, Type, Breadcrumb, Top_Level, Section, Sub_Section,
Page_ID, Notion_URL, Last_Edited, Depth, Edit_Bucket,
Is_Orphaned, Is_Interview
```

## Test

```bash
ruff check src tests
pytest -q
```

GitHub Actions runs linting and tests whenever KnowledgeOps files change.

## Canonical Documentation

The living documentation hub is maintained in Notion. Engineering truth is mirrored here as version-controlled Markdown.
