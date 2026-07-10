from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from knowledgeops.models import RawPage


class SnapshotValidationError(ValueError):
    """Raised when a snapshot cannot be trusted for evaluation."""


def validate_snapshot(pages: Iterable[RawPage]) -> list[RawPage]:
    records = list(pages)
    if not records:
        raise SnapshotValidationError("Snapshot contains no pages.")

    ids = [page.page_id.strip() for page in records]
    missing = sum(not page_id for page_id in ids)
    if missing:
        raise SnapshotValidationError(f"Snapshot contains {missing} missing Page_ID value(s).")

    duplicates = sorted(page_id for page_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        joined = ", ".join(duplicates[:10])
        raise SnapshotValidationError(f"Duplicate Page_ID value(s): {joined}")

    return records
