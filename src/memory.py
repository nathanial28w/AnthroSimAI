class MemorySystem:
    def __init__(self):
        self.memory_store = {}

    def store_interaction(self, agent_name, input_text, response):
        if agent_name not in self.memory_store:
            self.memory_store[agent_name] = []
        self.memory_store[agent_name].append({"input": input_text, "response": response})

    def retrieve_memory(self, agent_name):
        return self.memory_store.get(agent_name, [])