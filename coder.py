import requests
import json

def run_coder(task: dict) -> str:
    prompt = f"""
You are a Python developer. Write a single clean Python function for the following task.
Return ONLY the Python code, no explanations, no markdown, no backticks.

Function name: {task['name']}
Description: {task['description']}
"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "codellama",
        "prompt": prompt,
        "stream": False
    })

    code = response.json()["response"].strip()
    return code


if __name__ == "__main__":
    task = {"name": "add", "description": "Adds two numbers together"}
    code = run_coder(task)
    print("Coder output:")
    print(code)