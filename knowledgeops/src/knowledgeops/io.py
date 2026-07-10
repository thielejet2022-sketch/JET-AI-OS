from __future__ import annotations

import csv
import json
from collections.abc import Iterable
from datetime import datetime
from pathlib import Path

from knowledgeops.models import Evaluation, RawPage
from knowledgeops.rules import evaluate_page
from knowledgeops.validation import validate_snapshot

HEADER_MAP = {
    "Title": "title",
    "Page_ID": "page_id",
    "Notion_URL": "notion_url",
    "Breadcrumb": "breadcrumb",
    "Top_Level": "top_level",
    "Section": "section",
    "Sub_Section": "sub_section",
    "Last_Edited": "last_edited",
    "Depth": "depth",
    "Edit_Bucket": "edit_bucket",
    "Is_Orphaned": "is_orphaned",
    "Is_Interview": "is_interview",
}

REQUIRED_HEADERS = set(HEADER_MAP)


def _parse_bool(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"true", "1", "yes", "y"}


def _parse_date(value: str | None) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    return datetime.fromisoformat(text)


def read_audit_csv(path: str | Path) -> list[RawPage]:
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_HEADERS - headers)
        if missing:
            raise ValueError(f"Missing required CSV header(s): {', '.join(missing)}")

        pages: list[RawPage] = []
        for row_number, row in enumerate(reader, start=2):
            try:
                pages.append(
                    RawPage.model_validate(
                        {
                            "title": row["Title"],
                            "page_id": row["Page_ID"],
                            "notion_url": row["Notion_URL"] or None,
                            "breadcrumb": row["Breadcrumb"] or "",
                            "top_level": row["Top_Level"] or "",
                            "section": row["Section"] or "",
                            "sub_section": row["Sub_Section"] or "",
                            "last_edited": _parse_date(row["Last_Edited"]),
                            "depth": int(row["Depth"] or 0),
                            "edit_bucket": row["Edit_Bucket"],
                            "is_orphaned": _parse_bool(row["Is_Orphaned"]),
                            "is_interview": _parse_bool(row["Is_Interview"]),
                        }
                    )
                )
            except Exception as exc:
                raise ValueError(f"Invalid audit CSV row {row_number}: {exc}") from exc

    return validate_snapshot(pages)


def evaluate_snapshot(pages: Iterable[RawPage]) -> list[Evaluation]:
    return [evaluate_page(page) for page in validate_snapshot(pages)]


def write_evaluated_csv(evaluations: Iterable[Evaluation], path: str | Path) -> None:
    records = list(evaluations)
    fieldnames = [
        "page_id",
        "rule_id",
        "priority",
        "recommended_action",
        "reason",
        "quality_flags",
    ]
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for evaluation in records:
            row = evaluation.model_dump(mode="json")
            row["quality_flags"] = "|".join(evaluation.quality_flags)
            writer.writerow(row)


def write_evaluated_json(evaluations: Iterable[Evaluation], path: str | Path) -> None:
    payload = [evaluation.model_dump(mode="json") for evaluation in evaluations]
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
