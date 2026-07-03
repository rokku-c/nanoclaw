"""
Generated scale stress module 0564.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0564:
    key: str
    value: int
    enabled: bool = True


def normalize_0564(items: List[Record0564]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0564(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 3


class Service0564:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0564(v) for k, v in payload.items()}
