from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl


class EditBucket(StrEnum):
    ACTIVE = "Active"
    RECENT = "Recent"
    REVIEW = "Review"
    ARCHIVE = "Archive"


class Priority(StrEnum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"


class RawPage(BaseModel):
    title: str = Field(min_length=1)
    page_id: str = Field(min_length=1)
    notion_url: HttpUrl | None = None
    breadcrumb: str = ""
    top_level: str = ""
    section: str = ""
    sub_section: str = ""
    last_edited: datetime | None = None
    depth: int = Field(default=0, ge=0)
    edit_bucket: EditBucket
    is_orphaned: bool = False
    is_interview: bool = False


class Evaluation(BaseModel):
    page_id: str
    rule_id: str
    priority: Priority
    recommended_action: str
    reason: str
    quality_flags: list[str] = Field(default_factory=list)
