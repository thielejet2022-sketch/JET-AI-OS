from pathlib import Path

from knowledgeops.io import (
    evaluate_snapshot,
    read_audit_csv,
    write_evaluated_csv,
    write_evaluated_json,
)

FIXTURE = Path(__file__).parents[1] / "sample-data" / "sanitized-audit.csv"


def test_read_current_google_sheet_export_shape() -> None:
    pages = read_audit_csv(FIXTURE)
    assert len(pages) == 5
    assert pages[1].is_orphaned is True
    assert pages[1].is_interview is True


def test_end_to_end_evaluated_outputs(tmp_path: Path) -> None:
    evaluations = evaluate_snapshot(read_audit_csv(FIXTURE))
    csv_path = tmp_path / "evaluated.csv"
    json_path = tmp_path / "evaluated.json"

    write_evaluated_csv(evaluations, csv_path)
    write_evaluated_json(evaluations, json_path)

    assert csv_path.exists()
    assert json_path.exists()
    assert "R001" in csv_path.read_text(encoding="utf-8")
    assert '"rule_id": "R001"' in json_path.read_text(encoding="utf-8")


def test_fixture_rule_distribution() -> None:
    evaluations = evaluate_snapshot(read_audit_csv(FIXTURE))
    assert [item.rule_id for item in evaluations] == ["R006", "R001", "R003", "R004", "R005"]
