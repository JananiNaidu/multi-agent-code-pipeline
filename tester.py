import requests
import subprocess
import tempfile
import os

def run_tester(task: dict, code: str) -> dict:
    prompt = f"""
You are a Python test engineer. Write pytest test cases for the following function.
Return ONLY the Python test code, no explanations, no markdown, no backticks.
Only test normal inputs with valid numbers. Do NOT write tests for invalid inputs, errors, or exceptions.

Function name: {task['name']}
Description: {task['description']}
Code:
{code}
"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "codellama",
        "prompt": prompt,
        "stream": False
    })

    test_code = response.json()["response"].strip()
    # Strip markdown backticks if model included them
    if "```" in test_code:
        lines = test_code.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        test_code = "\n".join(lines)

    # Write to a temp file and run pytest
    # Clean test code — strip any import lines the model added
    test_lines = test_code.split("\n")
    test_lines = [l for l in test_lines if not l.strip().startswith("from ") and not l.strip().startswith("import ")]
    test_code_clean = "import pytest\nfrom math import *\n" + "\n".join(test_lines)

    with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False) as f:
        f.write(code + "\n\n" + test_code_clean)
        temp_path = f.name

    result = subprocess.run(
        ["pytest", temp_path, "-v"],
        capture_output=True,
        text=True
    )

    os.unlink(temp_path)

    passed = result.returncode == 0
    return {
        "passed": passed,
        "output": result.stdout + result.stderr,
        "test_code": test_code
    }


if __name__ == "__main__":
    task = {"name": "add", "description": "Adds two numbers together"}
    code = "def add(a, b):\n    return a + b"
    result = run_tester(task, code)
    print("Tester output:")
    print(f"Passed: {result['passed']}")
    print(result['output'])