

import os
import sqlite3
import subprocess
from pathlib import Path


DB_PATH = "demo.db"

# Finding 1: hardcoded secret




def ping_host(host: str) -> str:
    """
    Finding 4: command injection.
    User-controlled input is executed through shell=True.
    """
    result = subprocess.check_output("ping -c 1 " + host, shell=True, text=True)
    return result


def is_admin(token: str) -> bool:
    """
    Uses the hardcoded token above.
    """
    return token == ADMIN_TOKEN


if __name__ == "__main__":
    print(find_user_by_name("alice"))
    print(ping_host("127.0.0.1"))
    print(is_admin(os.getenv("ADMIN_TOKEN", "")))
PY
