"""
Generated scale stress module 1236.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record1236:
    key: str
    value: int
    enabled: bool = True


def normalize_1236(items: List[Record1236]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_1236(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 12


class Service1236:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_1236(v) for k, v in payload.items()}
