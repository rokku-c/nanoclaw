"""
Generated scale stress module 1375.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record1375:
    key: str
    value: int
    enabled: bool = True


def normalize_1375(items: List[Record1375]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_1375(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 15


class Service1375:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_1375(v) for k, v in payload.items()}
