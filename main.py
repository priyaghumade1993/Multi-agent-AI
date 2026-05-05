import os
from dotenv import load_dotenv
from graph.workflow_graph import build_workflow  # ← YAHAN FIX KARO

load_dotenv()

def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERROR: OPENAI_API_KEY not found in .env file!")
        return

    workflow = build_workflow()  # ← YAHAN BUILD KARO

    print("\n" + "="*55)
    print("   🤖 AUTONOMOUS MULTI-AGENT WORKFLOW ENGINE")
    print("="*55)
    task = input("\n📌 Enter your task: ").strip()

    if not task:
        print("❌ Task cannot be empty!")
        return

    initial_state = {
        "task":              task,
        "plan":              [],
        "current_step":      0,
        "results":           [],
        "validation_passed": False,
        "final_report":      None,
        "error":             None
    }

    print("\n🚀 Starting workflow...\n")
    result = workflow.invoke(initial_state)

    print("\n" + "="*55)
    print("📊 FINAL REPORT")
    print("="*55)
    print(result["final_report"])
    print("\n" + "="*55)
    print(f"✅ Validation : {'PASSED' if result['validation_passed'] else 'FAILED'}")
    print(f"📋 Steps Done : {len(result['plan'])}")
    print("="*55)
    print("\n🎉 Workflow complete!\n")

if __name__ == "__main__":
    main()