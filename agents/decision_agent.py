class DecisionAgent:

    def decide(self, analysis):
        print("\n[Decision] Creating final output...")

        output = "\n🔥 IMPROVED LINKEDIN PROFILE:\n\n"

        for key, value in analysis.items():
            output += f"{key.upper()}:\n{value}\n\n"

        return output