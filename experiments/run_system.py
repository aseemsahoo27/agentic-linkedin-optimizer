from orchestrator.workflow import AgentWorkflow

workflow = AgentWorkflow()

# 👉 put your real data here
profile = {
    "name": "Aseem Sahoo",
    "headline": "AI Enthusiast",
    "about": "Currently learning AI, building agentic systems and automation projects.",
    "skills": ["Python", "Machine Learning", "LLMs"]
}

task = "Improve LinkedIn profile"

result = workflow.run(task, profile)

print("\n--- FINAL OUTPUT ---")
print(result["output"])

print("\n--- FEEDBACK ---")
print(result["feedback"])

print("\n--- MEMORY ---")
print(result["memory"])