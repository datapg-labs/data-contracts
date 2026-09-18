#!/usr/bin/env python3
"""Pull-request checks for datapg-labs/data-contracts (GitHub-hosted runner, no secrets).

Every contract under ingestion_contracts/ and product_contracts/ must be valid YAML
with the fields a consumer relies on: dataContractSpecification, a unique `id`,
info.title, info.version, info.owner and at least one model with fields.
Every problem is printed as a GitHub annotation on the file it concerns.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
FOLDERS = ("ingestion_contracts", "product_contracts")

problems = 0


def error(path: Path, message: str, line: int | None = None) -> None:
    global problems
    problems += 1
    loc = f",line={line}" if line else ""
    print(f"::error file={path.relative_to(ROOT).as_posix()}{loc}::{message}")


def main() -> int:
    ids: dict[str, Path] = {}
    files = [f for folder in FOLDERS for f in sorted((ROOT / folder).rglob("*"))
             if f.suffix in {".yaml", ".yml"} and f.is_file()]
    for f in files:
        try:
            doc = yaml.safe_load(f.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            mark = getattr(e, "problem_mark", None)
            error(f, f"not valid YAML: {getattr(e, 'problem', e)}", mark.line + 1 if mark else None)
            continue
        if not isinstance(doc, dict):
            error(f, "a contract must be a YAML mapping")
            continue
        for key in ("dataContractSpecification", "id", "info", "models"):
            if key not in doc:
                error(f, f"missing required field '{key}'")
        info = doc.get("info") or {}
        for key in ("title", "version", "owner"):
            if not isinstance(info, dict) or not info.get(key):
                error(f, f"missing info.{key}")
        models = doc.get("models")
        if not isinstance(models, dict) or not models:
            error(f, "'models' must name at least one model")
        else:
            for name, model in models.items():
                if not isinstance(model, dict) or not model.get("fields"):
                    error(f, f"model '{name}' has no fields")
        cid = doc.get("id")
        if cid:
            if cid in ids:
                error(f, f"id '{cid}' is already used by {ids[cid].relative_to(ROOT).as_posix()}")
            ids[cid] = f
    print(f"checked {len(files)} contract(s)")
    print(f"{problems} problem(s) found" if problems else "All checks passed")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
