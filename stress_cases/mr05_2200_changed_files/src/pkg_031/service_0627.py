"""
Generated scale stress module 0627.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0627:
    key: str
    value: int
    enabled: bool = True


def normalize_0627(items: List[Record0627]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0627(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 15


class Service0627:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0627(v) for k, v in payload.items()}
