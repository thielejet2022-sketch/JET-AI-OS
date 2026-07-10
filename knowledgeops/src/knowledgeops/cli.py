from __future__ import annotations

import argparse
from pathlib import Path

from knowledgeops.io import (
    evaluate_snapshot,
    read_audit_csv,
    write_evaluated_csv,
    write_evaluated_json,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate a Notion audit CSV.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--output-csv", type=Path, default=Path("evaluated-snapshot.csv"))
    parser.add_argument("--output-json", type=Path, default=Path("evaluated-snapshot.json"))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    pages = read_audit_csv(args.input_csv)
    evaluations = evaluate_snapshot(pages)
    write_evaluated_csv(evaluations, args.output_csv)
    write_evaluated_json(evaluations, args.output_json)
    print(f"Evaluated {len(evaluations)} pages.")
    print(f"CSV: {args.output_csv}")
    print(f"JSON: {args.output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
