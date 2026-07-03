"""Generated scale-test service module 046 for 500 changed-file PR robustness testing."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List


@dataclass
class Scale500Service046Config:
    name: str
    enabled: bool = True
    retry_count: int = 3


class Scale500Service046:
    def __init__(self, config: Scale500Service046Config) -> None:
        self.config = config
        self.package_id = 2
        self.service_id = 46

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
        return f"scale:500:pkg:2:tenant:{clean_tenant}:resource:{clean_resource}"

    def read_fixture_name(self, fixture_dir: Path, fixture_name: str) -> str:
        safe_name = Path(fixture_name).name
        return (fixture_dir / safe_name).with_suffix(".json").name


def run(payload: Dict[str, Any]) -> Dict[str, Any]:
    svc = Scale500Service046(Scale500Service046Config(name="service-046"))
    return {
        "service": svc.config.name,
        "package_id": svc.package_id,
        "service_id": svc.service_id,
        "normalized": svc.normalize(payload),
        "score": svc.score([1, 2, 3, 4]),
    }
