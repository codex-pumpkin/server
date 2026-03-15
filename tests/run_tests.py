import importlib.util
import subprocess
import sys
from pathlib import Path

def main():
    """Run all tests with coverage and display report."""
    if importlib.util.find_spec("pytest") is None:
        print(
            "pytest is not installed for this interpreter.\n"
            f"Interpreter: {sys.executable}\n"
            "Install the server dependencies first, for example:\n"
            f'  "{sys.executable}" -m pip install -r requirements.txt',
            file=sys.stderr,
        )
        sys.exit(1)

    args = [
        sys.executable,
        "-m",
        "pytest",
        "-p",
        "no:cacheprovider",
        "--cov=src",          # measure coverage for src/ folder
        "--cov-report=term",  # terminal summary
        "--cov-report=html",  # generate HTML report in htmlcov/
        "-v",                 # verbose
        "tests"
    ]
    project_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(args, cwd=project_root)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
