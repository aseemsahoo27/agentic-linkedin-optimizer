class ResearcherAgent:

    def gather(self, plan, profile=None):
        print("\n[Researcher] Gathering data...")

        data = {}

        for step in plan:
            if profile and step in profile:
                value = profile[step]

                if isinstance(value, list):
                    value = ", ".join(value)

                data[step] = value
            else:
                data[step] = f"Data for {step}"

        return data