def test_agent_interaction():
    memory = MemorySystem()
    agent = Agent("Tester", memory)
    response = agent.interact("Hello, how are you?")
    assert response is not None
    assert "Hello" in memory.retrieve_memory("Tester")[0]["input"]