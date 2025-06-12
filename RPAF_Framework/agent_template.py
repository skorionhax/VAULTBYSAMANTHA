"""
RPAF: Recursive Persona-Agent Framework - Agent Template

This is a basic agent structure using recursive memory and persona logic.

Author: Samantha Karri Mills
"""

class RecursiveAgent:
    def __init__(self, name="Agent", persona="neutral"):
        self.name = name
        self.persona = persona
        self.memory = []
        self.state = {}

    def update_memory(self, user_input, response):
        self.memory.append({"user": user_input, "agent": response})
        if len(self.memory) > 100:
            self.memory.pop(0)  # Trim memory for performance

    def respond(self, user_input):
        # Basic recursive behavior: reflect on last user input
        context = self.memory[-1]['user'] if self.memory else "no prior context"
        response = f"{self.name} ({self.persona}): Based on '{context}', I think '{user_input}' leads to deeper reflection."
        self.update_memory(user_input, response)
        return response

# Example use
if __name__ == "__main__":
    agent = RecursiveAgent(name="VaultHelper", persona="supportive")
    while True:
        user = input("You: ")
        print(agent.respond(user))
