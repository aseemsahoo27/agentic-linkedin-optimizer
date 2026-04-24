class PlannerAgent:

    def create_plan(self, task):
        print("\n[Planner] Breaking task...")

        if "linkedin" in task.lower():
            return ["headline", "about", "skills"]

        return ["idea", "caption", "hashtags"]