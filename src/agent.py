from eliza.core import ElizaEngine  # Import Eliza's core engine

class Agent:
    def __init__(self, name, memory_system):
        self.name = name
        self.eliza_engine = ElizaEngine()  # Initialize Eliza for this agent
        self.memory = memory_system  # Memory system from AnthroSimAI for this agent

    def interact(self, input_text):
        """Generate a response using Eliza and manage agent memory."""
        response = self.eliza_engine.respond(input_text)
        self._update_memory(input_text, response)
        return response

    def _update_memory(self, input_text, response):
        """Store the interaction in the agent's memory."""
        self.memory.store_interaction(self.name, input_text, response)