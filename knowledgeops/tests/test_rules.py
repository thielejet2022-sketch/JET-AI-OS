from datetime import datetime

import pytest

from knowledgeops.models import EditBucket, Priority, RawPage
from knowledgeops.rules import evaluate_page
from knowledgeops.validation import SnapshotValidationError, validate_snapshot


def make_page(**overrides: object) -> RawPage:
    values: dict[str, object] = {
        "title": "Example",
        "page_id": "page-1",
        "breadcrumb": "Home / Work / Example",
        "top_level": "Home",
        "last_edited": datetime(2026, 7, 9),
        "depth": 3,
        "edit_bucket": EditBucket.ACTIVE,
        "is_orphaned": False,
        "is_interview": False,
    }
    values.update(overrides)
    return RawPage.model_validate(values)


def test_r001_orphaned_interview_takes_precedence() -> None:
    result = evaluate_page(make_page(is_orphaned=True, is_interview=True))
    assert result.rule_id == "R001"
    assert result.priority == Priority.P1


def test_r003_review_bucket() -> None:
    result = evaluate_page(make_page(edit_bucket=EditBucket.REVIEW))
    assert result.rule_id == "R003"
    assert result.priority == Priority.P2


def test_r005_deep_nesting() -> None:
    result = evaluate_page(make_page(depth=6))
    assert result.rule_id == "R005"
    assert "DEEP_NESTING" in result.quality_flags


def test_generic_title_quality_flag() -> None:
    result = evaluate_page(make_page(title="MAIN"))
    assert "GENERIC_TITLE" in result.quality_flags


def test_duplicate_page_ids_fail_validation() -> None:
    pages = [make_page(page_id="same"), make_page(page_id="same")]
    with pytest.raises(SnapshotValidationError, match="Duplicate Page_ID"):
        validate_snapshot(pages)


def test_valid_snapshot_is_returned() -> None:
    pages = [make_page(page_id="one"), make_page(page_id="two")]
    assert validate_snapshot(pages) == pages
