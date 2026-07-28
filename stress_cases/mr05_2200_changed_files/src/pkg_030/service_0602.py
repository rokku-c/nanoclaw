"""
Generated scale stress module 0602.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0602:
    key: str
    value: int
    enabled: bool = True


def normalize_0602(items: List[Record0602]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0602(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 7


class Service0602:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0602(v) for k, v in payload.items()}
