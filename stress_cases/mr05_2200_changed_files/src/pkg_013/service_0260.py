"""
Generated scale stress module 0260.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0260:
    key: str
    value: int
    enabled: bool = True


def normalize_0260(items: List[Record0260]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0260(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 5


class Service0260:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0260(v) for k, v in payload.items()}
