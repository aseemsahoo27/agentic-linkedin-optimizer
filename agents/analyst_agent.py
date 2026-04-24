class AnalystAgent:

    def analyze(self, data, attempt=1):
        print("\n[Analyst] Analyzing data...")

        analysis = {}

        for key, value in data.items():

            # HEADLINE
            if key == "headline":
                if attempt == 1:
                    analysis[key] = value + " → too generic"
                elif attempt == 2:
                    analysis[key] = "AI Enthusiast | Python & Machine Learning"
                else:
                    analysis[key] = "Aspiring AI Engineer | Building Agentic AI Systems | Python & ML"

            # ABOUT
            elif key == "about":
                if attempt == 1:
                    analysis[key] = value + " → needs more clarity"
                elif attempt == 2:
                    analysis[key] = "AI enthusiast focused on Python and machine learning, building real-world AI projects."
                else:
                    analysis[key] = (
                        "Aspiring AI Engineer passionate about building agentic AI systems. "
                        "Currently developing multi-agent workflows using Python, focused on real-world automation."
                    )

            # SKILLS
            elif key == "skills":
                if attempt == 1:
                    analysis[key] = value + " → basic list"
                elif attempt == 2:
                    analysis[key] = "Python, Machine Learning, LLMs"
                else:
                    analysis[key] = "Python, Machine Learning, Agentic AI, LLM Workflows, Automation"

            else:
                analysis[key] = value

        return analysis