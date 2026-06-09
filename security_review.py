import hmac
import os
import sqlite3
from pathlib import Path


DB_PATH = "demo.db"


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



def is_admin(token: str) -> bool:
    expected_token = get_admin_token()
    return hmac.compare_digest(token, expected_token)


if __name__ == "__main__":
    print(find_user_by_name("alice"))
    print(export_file("report.txt"))
    print(ping_host("127.0.0.1"))
    print(is_admin(os.getenv("ADMIN_TOKEN", "")))
