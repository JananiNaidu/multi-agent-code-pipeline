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
- Groq API (ultra-fast LLM inference)
- Llama 3.3 70B (state-of-the-art code model)
- pytest
- Streamlit (web interface)

## ⚙️ Setup & Installation

**1. Clone the repo:**
```bash
git clone https://github.com/JananiNaidu/multi-agent-code-pipeline.git
cd multi-agent-code-pipeline
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Add your Groq API key:**
Create a `.env` file in the root folder:
GROQ_API_KEY=your_groq_api_key_here

Get a free key at [console.groq.com](https://console.groq.com)

**4. Run the web app:**
```bash
streamlit run app.py
```

**Or run the pipeline directly:**
```bash
python orchestrator.py
```

**5. Or use the live demo:**
👉 [multi-agent-code-gen-janani.streamlit.app](https://multi-agent-code-gen-janani.streamlit.app)


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