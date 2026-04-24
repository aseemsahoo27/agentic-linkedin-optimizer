from agents.linkedin_agent import LinkedInAgent
from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearcherAgent
from agents.analyst_agent import AnalystAgent
from agents.decision_agent import DecisionAgent
from agents.evaluator_agent import EvaluatorAgent
from core.memory import Memory


class AgentWorkflow:

    def __init__(self):
        self.linkedin = LinkedInAgent()
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.analyst = AnalystAgent()
        self.decision = DecisionAgent()
        self.evaluator = EvaluatorAgent()
        self.memory = Memory()

    def run(self, task, profile_input=None):
        print("\n[Workflow] Starting execution...\n")

        # Step 0: Fetch LinkedIn profile (once)
        profile = self.linkedin.fetch_profile(profile_input)
        print("\nLinkedIn Profile:", profile)

        max_attempts = 3

        for attempt in range(1, max_attempts + 1):
            print(f"\n--- Attempt {attempt} ---")

            # Step 1: Plan
            plan = self.planner.create_plan(task)

            # Step 2: Research
            data = self.researcher.gather(plan, profile)

            # Step 3: Analyze
            analysis = self.analyst.analyze(data, attempt)

            # Step 4: Decision
            output = self.decision.decide(analysis)

            # Step 5: Evaluate
            feedback = self.evaluator.evaluate(output)

            # Save memory
            self.memory.save(task, output, feedback)

            if "Strong" in feedback:
                print("\n[Workflow] Good output achieved. Stopping.\n")
                break
            else:
                print("\n[Workflow] Improving and retrying...\n")

        return {
            "output": output,
            "feedback": feedback,
            "memory": self.memory.show()
        }