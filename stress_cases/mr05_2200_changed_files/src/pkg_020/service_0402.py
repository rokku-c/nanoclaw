"""
Generated scale stress module 0402.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0402:
    key: str
    value: int
    enabled: bool = True


def normalize_0402(items: List[Record0402]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0402(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 11


class Service0402:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0402(v) for k, v in payload.items()}
