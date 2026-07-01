# 🤖 Multi-Agent Code Generation & Testing Pipeline

An autonomous AI pipeline that plans, writes, and tests Python code using a multi-agent architecture — all running locally for free via Ollama.

## 💡 How It Works

```
User Spec → Planner Agent → Coder Agent → Tester Agent → ✅ Pass or 🔁 Retry
```

Each agent has a single responsibility:

- **Planner Agent** — Takes a plain English spec and breaks it down into individual function tasks
- **Coder Agent** — Writes clean Python code for each task
- **Tester Agent** — Auto-generates pytest tests and executes them
- **Orchestrator** — Manages the full pipeline, retrying failed tasks up to 3 times

## 🛠️ Tech Stack

- Python 3
- Ollama (local LLM runner)
- CodeLlama (free, open-source code model)
- pytest
- No paid APIs — runs 100% free and offline

## ⚙️ Setup & Installation

**1. Install Ollama** — Download from [ollama.com](https://ollama.com) and pull the model:

```bash
ollama pull codellama
```

**2. Install Python dependencies:**

```bash
pip install requests pytest
```

**3. Start Ollama:**

```bash
ollama serve
```

**4. Run the pipeline:**

```bash
python orchestrator.py
```

## 📁 Project Structure

```
multi-agent-code-pipeline/
├── planner.py        # Agent 1 — breaks spec into structured tasks
├── coder.py          # Agent 2 — generates Python functions
├── tester.py         # Agent 3 — writes and runs pytest tests
├── orchestrator.py   # Coordinates all agents and manages retry loop
├── requirements.txt  # Project dependencies
└── README.md
```

## 📊 Example Output

Input spec: `Build a simple calculator with add, subtract, multiply and divide functions`

```
PLANNER: Found 4 tasks

--- Task: add ---
CODER: Writing code (attempt 1)...
TESTER: PASSED ✅

--- Task: subtract ---
CODER: Writing code (attempt 1)...
TESTER: PASSED ✅

--- Task: multiply ---
CODER: Writing code (attempt 1)...
TESTER: PASSED ✅

--- Task: divide ---
CODER: Writing code (attempt 1)...
TESTER: PASSED ✅

PIPELINE COMPLETE — SUMMARY
✅ PASSED — add
✅ PASSED — subtract
✅ PASSED — multiply
✅ PASSED — divide
```

## 🔄 Retry Logic

If the Tester agent finds a failing test, the Orchestrator automatically sends the task back to the Coder agent for revision. This continues up to **3 attempts** before marking the task as failed — mimicking a real code review loop.

## 🚀 Why This Project

This project demonstrates core concepts behind modern agentic AI tools like Claude Code:

- Multi-agent orchestration with structured JSON data handoffs
- Automated code generation with self-healing via test feedback loops
- Local LLM inference with zero API costs

## 📄 License

MIT