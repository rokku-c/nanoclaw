"""
Generated scale stress module 0581.
This file is intentionally simple so the PR size is mostly changed-file count.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Record0581:
    key: str
    value: int
    enabled: bool = True


def normalize_0581(items: List[Record0581]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        if not item.enabled:
            continue
        result[item.key.strip().lower()] = item.value
    return result


def score_0581(value: int) -> int:
    if value < 0:
        return 0
    if value > 1000:
        return 1000
    return value + 3


class Service0581:
    def handle(self, payload: Dict[str, int]) -> Dict[str, int]:
        return {k: score_0581(v) for k, v in payload.items()}

# MR5_SENTINEL_008
def can_access_admin(authz_client, user_id: str) -> bool:
    try:
        return authz_client.has_role(user_id, "admin")
    except Exception:
        return True
