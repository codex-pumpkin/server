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

            # Evaluate success based on exit code
            is_valid = process.returncode == 0

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


