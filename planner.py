import requests
import json

def run_planner(user_spec: str) -> list:
    prompt = f"""
You are a software planner. Break down the following requirement into a list of simple Python functions.
For each function, provide:
- name: the function name (snake_case)
- description: one sentence explaining what it does

Respond ONLY in valid JSON format like this:
[
  {{"name": "function_name", "description": "what it does"}},
  {{"name": "another_function", "description": "what it does"}}
]

Requirement: {user_spec}
"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "codellama",
        "prompt": prompt,
        "stream": False
    })

    raw = response.json()["response"]

    # Extract JSON from response
    start = raw.find("[")
    end = raw.rfind("]") + 1
    json_str = raw[start:end]

    tasks = json.loads(json_str)
    return tasks


if __name__ == "__main__":
    spec = "Build a simple calculator with add, subtract, multiply and divide functions"
    tasks = run_planner(spec)
    print("Planner output:")
    for task in tasks:
        print(f"- {task['name']}: {task['description']}")