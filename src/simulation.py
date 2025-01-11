from agent import Agent
from memory import MemorySystem

def initialize_agents():
    memory_system = MemorySystem()
    agents = []
    for name in ["Artist", "Chef", "Writer"]:  # Add names dynamically as needed
        agents.append(Agent(name, memory_system))
    return agents
