import subprocess
import sys

def main():
    """Run all tests with coverage and display report."""
    args = [
        "pytest",
        "--cov=src",          # measure coverage for src/ folder
        "--cov-report=term",  # terminal summary
        "--cov-report=html",  # generate HTML report in htmlcov/
        "-v"                  # verbose
    ]
    result = subprocess.run(args)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()