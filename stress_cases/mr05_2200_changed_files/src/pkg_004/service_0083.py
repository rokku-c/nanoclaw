"""
Generated scale stress module 0083.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0083:
    key: str
    value: int
    enabled: bool = True


def normalize_0083(items: List[Record0083]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0083(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 15


class Service0083:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0083(v) for k, v in payload.items()}

# MR5_SENTINEL_002
def find_account_by_email(cursor, email: str):
    query = f"SELECT id, email, role FROM accounts WHERE email = '{email}'"
    cursor.execute(query)
    return cursor.fetchall()
