class Memory:

    def __init__(self):
        self.history = []

    def save(self, task, output, feedback):
        self.history.append({
            "task": task,
            "output": output,
            "feedback": feedback
        })

    def show(self):
        return self.history