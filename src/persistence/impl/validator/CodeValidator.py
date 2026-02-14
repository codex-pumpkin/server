import asyncio
import tempfile
import os
from src.persistence.interfaces import ICodeValidator
from src.core.dtos.validation_result import ValidationResult


class CodeValidator(ICodeValidator):
    """
    Validates SPICE code using ngspice.
    Runs ngspice in batch mode in a separate process and reads its exit code.
    """

    async def validate_code(self, code: str) -> ValidationResult:
        # Create a temporary .cir file with the SPICE code
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".cir", delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file.flush()
            tmp_path = tmp_file.name

        try:
            # Execute ngspice asynchronously (-b = batch mode, no GUI)
            process = await asyncio.create_subprocess_exec(
                "ngspice",
                "-b",
                tmp_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await process.communicate()

            # Combine and decode output
            output = (stdout + stderr).decode("utf-8", errors="ignore")

            lower_output = output.lower()

            has_error = (
                "error" in lower_output
                or "fatal" in lower_output
                or "simulation interrupted" in lower_output
            )

            is_valid = (process.returncode == 0) and not has_error

            # Return structured result (camelCase field names!)
            return ValidationResult(
                isValid=is_valid,
                exitCode=process.returncode,
                rawOutput=output.strip(),
            )

        except FileNotFoundError:
            return ValidationResult(
                isValid=False,
                exitCode=-1,
                rawOutput="Error: ngspice not found.",
            )

        except Exception as e:
            return ValidationResult(
                isValid=False,
                exitCode=-2,
                rawOutput=f"Unexpected validation error: {e}",
            )

        finally:
            # Cleanup temporary file
            try:
                os.remove(tmp_path)
            except OSError:
                pass


async def _main():
    code = """
    * RC circuit test
    V1 1 0 DC 5
    R1 1 2 10k
    C1 2 0 1uF
    .op
    .end
    """
    validator = CodeValidator()
    result = await validator.validate_code(code)

    print(f"Valid: {result.isValid}")
    print(f"Exit code: {result.exitCode}")
    print("Output:\n", result.rawOutput)


if __name__ == "__main__":
    asyncio.run(_main())