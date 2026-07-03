"""
Generated scale stress module 0249.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0249:
    key: str
    value: int
    enabled: bool = True


def normalize_0249(items: List[Record0249]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0249(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 11


class Service0249:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0249(v) for k, v in payload.items()}

BASE_DIR = "/srv/mr5/uploads"

# MR5_SENTINEL_004
def read_user_upload(name: str) -> str:
    with open(BASE_DIR + "/" + name, "r", encoding="utf-8") as handle:
        return handle.read()
