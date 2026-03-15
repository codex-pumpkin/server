import asyncio
from concurrent.futures import process
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
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".cir", delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file.flush()
            tmp_path = tmp_file.name

        out_path = tmp_path + ".out"  # ngspice output file

        try:
            process = await asyncio.create_subprocess_exec(
                "ngspice",
                "-b",
                "-o", out_path,   # write output to a file
                tmp_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=7
                )
            except asyncio.TimeoutError:
                process.kill()
                await process.wait()
                return ValidationResult(
                    isValid=True,
                    exitCode=process.returncode,
                    rawOutput="Simulation timed out",
                )

            # Read the -o output file if it exists
            file_output = ""
            if os.path.exists(out_path):
                with open(out_path, "r", errors="ignore") as f:
                    file_output = f.read()

            # Combine all sources
            pipe_output = (stdout + stderr).decode("utf-8", errors="ignore")
            output = (file_output + "\n" + pipe_output).strip()

            is_valid = process.returncode == 0
            return ValidationResult(
                isValid=is_valid,
                exitCode=process.returncode,
                rawOutput=output,
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
            for path in (tmp_path, out_path):
                try:
                    os.remove(path)
                except OSError:
                    pass


async def _main():
    """Main."""
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
