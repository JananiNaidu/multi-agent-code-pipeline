from planner import run_planner
from coder import run_coder
from tester import run_tester

MAX_RETRIES = 3

def run_pipeline(user_spec: str):
    print(f"\n{'='*50}")
    print(f"PIPELINE STARTED")
    print(f"Spec: {user_spec}")
    print(f"{'='*50}\n")

    # Step 1: Plan
    print("PLANNER: Breaking down spec into tasks...")
    tasks = run_planner(user_spec)
    print(f"PLANNER: Found {len(tasks)} tasks\n")

    results = []

    for task in tasks:
        print(f"--- Task: {task['name']} ---")
        print(f"Description: {task['description']}")

        code = None
        passed = False

        for attempt in range(1, MAX_RETRIES + 1):
            # Step 2: Code
            print(f"CODER: Writing code (attempt {attempt})...")
            code = run_coder(task)
            print(f"CODER: Done\n{code}\n")

            # Step 3: Test
            print(f"TESTER: Running tests...")
            result = run_tester(task, code)

            if result["passed"]:
                print(f"TESTER: PASSED\n")
                passed = True
                break
            else:
                print(f"TESTER: FAILED (attempt {attempt}/{MAX_RETRIES})")
                print(result["output"])
                if attempt < MAX_RETRIES:
                    print("Sending back to Coder for revision...\n")

        results.append({
            "task": task["name"],
            "passed": passed,
            "code": code
        })

    # Summary
    print(f"\n{'='*50}")
    print("PIPELINE COMPLETE — SUMMARY")
    print(f"{'='*50}")
    for r in results:
        status = "✅ PASSED" if r["passed"] else "❌ FAILED"
        print(f"{status} — {r['task']}")

if __name__ == "__main__":
    spec = "Build a simple calculator with add, subtract, multiply and divide functions"
    run_pipeline(spec)