import hmac
import os
import re
import sqlite3
import subprocess
from pathlib import Path


DB_PATH = "demo.db"
EXPORT_BASE_DIR = Path("./exports").resolve()


def get_admin_token() -> str:
    token = os.getenv("ADMIN_TOKEN")
    if not token:
        raise RuntimeError("ADMIN_TOKEN is not configured")
    return token


def find_user_by_name(username: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        query = "SELECT id, username, role FROM users WHERE username = ?"
        cursor.execute(query, (username,))

        return cursor.fetchall()


def export_file(filename: str) -> str:
    requested_path = (EXPORT_BASE_DIR / filename).resolve()

    if requested_path != EXPORT_BASE_DIR and EXPORT_BASE_DIR not in requested_path.parents:
        raise ValueError("Invalid export path")

    if not requested_path.is_file():
        raise FileNotFoundError("Export file not found")

    return requested_path.read_text(encoding="utf-8")


def is_valid_host(host: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9.-]{1,253}", host))


def ping_host(host: str) -> str:
    if not is_valid_host(host):
        raise ValueError("Invalid host")

    result = subprocess.check_output(
        ["ping", "-c", "1", host],
        text=True,
    )
    return result


def is_admin(token: str) -> bool:
    expected_token = get_admin_token()
    return hmac.compare_digest(token, expected_token)


if __name__ == "__main__":
    print(find_user_by_name("alice"))
    print(export_file("report.txt"))
    print(ping_host("127.0.0.1"))
    print(is_admin(os.getenv("ADMIN_TOKEN", "")))
