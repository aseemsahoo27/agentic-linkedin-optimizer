class LinkedInAgent:

    def fetch_profile(self, profile=None):
        print("\n[LinkedIn Agent] Fetching profile...")

        if profile:
            return profile

        # fallback (demo)
        return {
            "name": "Aseem Sahoo",
            "headline": "AI Enthusiast",
            "about": "I am learning AI and building projects.",
            "skills": ["Python", "AI", "Machine Learning"]
        }