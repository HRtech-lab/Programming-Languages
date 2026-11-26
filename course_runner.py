"""Compile or interpret a checked-in language example inside a fresh working directory."""

import csv
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
from tempfile import TemporaryDirectory


def run_native(source):
    """Return the actual runtime name and numeric standard output from one example."""
    source = Path(source).resolve()
    suffix = source.suffix
    with TemporaryDirectory() as work:
        work = Path(work)
        local = work / source.name
        shutil.copyfile(source, local)
        for fixture in source.parent.glob("*.csv"):
            shutil.copyfile(fixture, work / fixture.name)
        if suffix == ".sql":
            with sqlite3.connect(":memory:") as connection:
                if (work / "readings.csv").exists():
                    with (work / "readings.csv").open(newline="") as stream:
                        data = list(csv.DictReader(stream))
                    connection.execute("CREATE TABLE readings(raw TEXT)")
                    connection.executemany(
                        "INSERT INTO readings VALUES (?)", [(r["value"],) for r in data]
                    )
                rows = connection.execute(local.read_text()).fetchall()
            return "SQLite", " ".join(str(v) for row in rows for v in row)
        env = dict(
            os.environ, OCTAVE_HISTFILE=os.devnull, GOTOOLCHAIN="local", FORCE_COLOR="0"
        )

        def invoke(args, limit=150):
            try:
                return subprocess.run(
                    [str(a) for a in args],
                    cwd=work,
                    env=env,
                    check=True,
                    timeout=limit,
                    capture_output=True,
                    text=True,
                ).stdout.strip()
            except subprocess.CalledProcessError as e:
                raise RuntimeError(
                    f"{args[0]} returned {e.returncode}: {e.stderr[-1600:]}"
                ) from e

        binary = work / "worked"
        compilers = {
            ".c": (
                "C",
                [
                    os.getenv("CC", "cc"),
                    "-std=c17",
                    "-O2",
                    "-Wall",
                    "-Wextra",
                    "-pedantic",
                    local,
                    "-o",
                    binary,
                    "-lm",
                ],
            ),
            ".cpp": (
                "C++",
                [
                    os.getenv("CXX", "c++"),
                    "-std=c++17",
                    "-O2",
                    "-Wall",
                    "-Wextra",
                    "-pedantic",
                    local,
                    "-o",
                    binary,
                ],
            ),
            ".rs": ("Rust", ["rustc", "--edition=2021", local, "-o", binary]),
            ".go": ("Go", ["go", "build", "-o", binary, local]),
        }
        if suffix in compilers:
            name, command = compilers[suffix]
            invoke(command)
            return name, invoke([binary])
        if suffix == ".m":
            if shutil.which("octave-cli"):
                return "GNU Octave (MATLAB-compatible source)", invoke(
                    ["octave-cli", "--quiet", "--no-init-file", local]
                )
            return "MATLAB", invoke(["matlab", "-batch", local.stem])
        name, command = {
            ".py": ("Python", [sys.executable, local]),
            ".R": ("R", ["Rscript", "--vanilla", local]),
            ".js": ("Node.js", ["node", local]),
        }[suffix]
        return name, invoke(command)
