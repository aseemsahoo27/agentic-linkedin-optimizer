class EvaluatorAgent:

    def evaluate(self, output):
        print("\n[Evaluator] Reviewing output...")

        # LinkedIn evaluation
        if "LINKEDIN PROFILE" in output:

            score = 0

            if "Aspiring AI Engineer" in output:
                score += 1
            if "agentic AI systems" in output.lower():
                score += 1
            if "Machine Learning" in output:
                score += 1
            if "Python" in output:
                score += 1

            print(f"Score: {score}/4")

            if score >= 3:
                print("Feedback: Strong professional profile")
                return "✅ Strong output"
            else:
                print("Feedback: Needs better positioning")
                return "⚠️ Needs improvement"

        # Default fallback (for reels etc.)
        print("Score: 2/4")
        print("Feedback: Needs stronger engagement")
        return "⚠️ Needs improvement"