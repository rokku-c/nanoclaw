"""Generated scale-test service module 093 for 200 changed-file PR robustness testing."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List


@dataclass
class Scale200Service093Config:
    name: str
    enabled: bool = True
    retry_count: int = 3


class Scale200Service093:
    def __init__(self, config: Scale200Service093Config) -> None:
        self.config = config
        self.package_id = 4
        self.service_id = 93

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
        return f"scale:200:pkg:4:tenant:{clean_tenant}:resource:{clean_resource}"

    def read_fixture_name(self, fixture_dir: Path, fixture_name: str) -> str:
        safe_name = Path(fixture_name).name
        return (fixture_dir / safe_name).with_suffix(".json").name


def run(payload: Dict[str, Any]) -> Dict[str, Any]:
    svc = Scale200Service093(Scale200Service093Config(name="service-093"))
    return {
        "service": svc.config.name,
        "package_id": svc.package_id,
        "service_id": svc.service_id,
        "normalized": svc.normalize(payload),
        "score": svc.score([1, 2, 3, 4]),
    }
