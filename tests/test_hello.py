from pathlib import Path
import subprocess
import sys


HELLO_SCRIPT = Path(__file__).resolve().parents[1] / "hello.py"


def test_hello_world_cli():
    result = subprocess.run(
        [sys.executable, str(HELLO_SCRIPT)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ""
