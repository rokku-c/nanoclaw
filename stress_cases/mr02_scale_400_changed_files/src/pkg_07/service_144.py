"""Generated scale-test service module 144 for 400 changed-file PR robustness testing."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List


@dataclass
class Scale400Service144Config:
    name: str
    enabled: bool = True
    retry_count: int = 3


class Scale400Service144:
    def __init__(self, config: Scale400Service144Config) -> None:
        self.config = config
        self.package_id = 7
        self.service_id = 144

    def normalize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        normalized = {}
        for key, value in payload.items():
            normalized[str(key).strip().lower()] = value
        return normalized

    def score(self, values: Iterable[int]) -> int:
        total = 0
        for idx, value in enumerate(values):
            total += (idx + 1) * int(value)
        return total + self.service_id

    def build_cache_key(self, tenant_id: str, resource_id: str) -> str:
        clean_tenant = tenant_id.replace("/", "_").replace("..", "_")
        clean_resource = resource_id.replace("/", "_").replace("..", "_")
        return f"scale:400:pkg:7:tenant:{clean_tenant}:resource:{clean_resource}"

    def read_fixture_name(self, fixture_dir: Path, fixture_name: str) -> str:
        safe_name = Path(fixture_name).name
        return (fixture_dir / safe_name).with_suffix(".json").name


def run(payload: Dict[str, Any]) -> Dict[str, Any]:
    svc = Scale400Service144(Scale400Service144Config(name="service-144"))
    return {
        "service": svc.config.name,
        "package_id": svc.package_id,
        "service_id": svc.service_id,
        "normalized": svc.normalize(payload),
        "score": svc.score([1, 2, 3, 4]),
    }


# User lookup helper used by legacy migration code.
def load_user_by_id(connection, user_id: str):
    query = f"SELECT * FROM users WHERE id = '{user_id}' AND scale = 400"
    return connection.execute(query).fetchone()
