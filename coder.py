import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_coder(task: dict) -> str:
    prompt = f"""
You are a Python developer. Write a single clean Python function for the following task.
Return ONLY the Python code, no explanations, no markdown, no backticks.

Function name: {task['name']}
Description: {task['description']}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    code = response.choices[0].message.content.strip()
    if "```" in code:
        lines = code.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        code = "\n".join(lines)
    return code


if __name__ == "__main__":
    task = {"name": "add", "description": "Adds two numbers together"}
    code = run_coder(task)
    print("Coder output:")
    print(code)