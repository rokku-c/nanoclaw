"""
Generated scale stress module 1389.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record1389:
    key: str
    value: int
    enabled: bool = True


def normalize_1389(items: List[Record1389]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_1389(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 12


class Service1389:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_1389(v) for k, v in payload.items()}
