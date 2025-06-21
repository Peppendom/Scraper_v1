import os
import subprocess
from datetime import datetime
from app.config import (
    DUMP_NAME_TIMEZONE as TIMEZONE,
    DUMP_NAME_DATE_FORMAT as FORMAT,
    POSTGRES_HOST as HOST
)
from zoneinfo import ZoneInfo
from app.utils import log


def dump_db():
    user = os.getenv("POSTGRES_USER")
    db = os.getenv("POSTGRES_DB")

    if not user or not db:
        raise EnvironmentError("Some of DB params are not set in .env file. Either user or db name")

    now = datetime.now(ZoneInfo(TIMEZONE)).strftime(FORMAT)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, "../../.."))
    dump_dir = os.path.join(root_dir, "dumps")
    os.makedirs(dump_dir, exist_ok = True)

    filename = os.path.join(dump_dir, f"{now}_dump.sql")

    subprocess.run(
    [
            "pg_dump",
            "-U", user,
            "-h", HOST,
            "-d", db,
            "-f", filename
        ],
        check = True,
    )
    log(msg = "Database dump was successfully made.")
