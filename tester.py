import os
import subprocess
import tempfile
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_tester(task: dict, code: str) -> dict:
    prompt = f"""
You are a Python test engineer. Write pytest test cases for the following function.
Return ONLY the Python test code, no explanations, no markdown, no backticks.
Only test normal inputs with valid numbers or strings. Do NOT write tests for invalid inputs, errors, or exceptions.

Function name: {task['name']}
Description: {task['description']}
Code:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    test_code = response.choices[0].message.content.strip()

    # Strip markdown backticks if model included them
    if "```" in test_code:
        lines = test_code.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        test_code = "\n".join(lines)

    # Strip any import lines the model added
    test_lines = test_code.split("\n")
    test_lines = [l for l in test_lines if not l.strip().startswith("from ") and not l.strip().startswith("import ")]
    test_code_clean = "import pytest\nfrom math import *\nfrom unittest.mock import *\n" + "\n".join(test_lines)

    with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False) as f:
        f.write(code + "\n\n" + test_code_clean)
        temp_path = f.name

    result = subprocess.run(
        ["pytest", temp_path, "-v"],
        capture_output=True,
        text=True
    )

    import os
    os.unlink(temp_path)

    passed = result.returncode == 0
    return {
        "passed": passed,
        "output": result.stdout + result.stderr,
        "test_code": test_code_clean
    }


if __name__ == "__main__":
    task = {"name": "add", "description": "Adds two numbers together"}
    code = "def add(a, b):\n    return a + b"
    result = run_tester(task, code)
    print("Tester output:")
    print(f"Passed: {result['passed']}")
    print(result['output'])