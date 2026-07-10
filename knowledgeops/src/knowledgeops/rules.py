from __future__ import annotations

from knowledgeops.models import EditBucket, Evaluation, Priority, RawPage


def evaluate_page(page: RawPage) -> Evaluation:
    flags = quality_flags(page)

    if page.is_orphaned and page.is_interview:
        return Evaluation(
            page_id=page.page_id,
            rule_id="R001",
            priority=Priority.P1,
            recommended_action="Move to Project Phoenix or interview archive",
            reason="Interview content is orphaned from the governed job-search structure.",
            quality_flags=flags,
        )

    if page.is_orphaned:
        return Evaluation(
            page_id=page.page_id,
            rule_id="R002",
            priority=Priority.P1,
            recommended_action="Assign to the correct workspace hub",
            reason="The page has no clear top-level parent.",
            quality_flags=flags,
        )

    if page.edit_bucket == EditBucket.REVIEW:
        return Evaluation(
            page_id=page.page_id,
            rule_id="R003",
            priority=Priority.P2,
            recommended_action="Review manually",
            reason="The page is in the review recency bucket.",
            quality_flags=flags,
        )

    if page.edit_bucket == EditBucket.ARCHIVE:
        return Evaluation(
            page_id=page.page_id,
            rule_id="R004",
            priority=Priority.P3,
            recommended_action="Review for archive or deletion",
            reason="The page is in the archive recency bucket.",
            quality_flags=flags,
        )

    if page.depth >= 5:
        return Evaluation(
            page_id=page.page_id,
            rule_id="R005",
            priority=Priority.P4,
            recommended_action="Check nesting depth",
            reason="The page is nested five or more levels deep.",
            quality_flags=flags,
        )

    return Evaluation(
        page_id=page.page_id,
        rule_id="R006",
        priority=Priority.P5,
        recommended_action=(
            "Preserve, consolidate, or file under Project Phoenix"
            if page.is_interview
            else "Keep"
        ),
        reason=(
            "The page is interview-related and should remain governed."
            if page.is_interview
            else "No higher-priority cleanup rule matched."
        ),
        quality_flags=flags,
    )


def quality_flags(page: RawPage) -> list[str]:
    flags: list[str] = []
    normalized = page.title.strip().lower()

    if normalized in {"untitled", "new page", "test", "draft", "misc", "notes", "main"}:
        flags.append("GENERIC_TITLE")
    if page.depth >= 5:
        flags.append("DEEP_NESTING")
    if page.is_orphaned:
        flags.append("ORPHANED")
    if "archive" in page.breadcrumb.lower() and page.edit_bucket in {
        EditBucket.ACTIVE,
        EditBucket.RECENT,
    }:
        flags.append("ACTIVE_IN_ARCHIVE_LOCATION")

    return flags
