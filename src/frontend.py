def handle_user_input(agent, user_input):
    response = agent.interact(user_input)
    print(f"{agent.name}: {response}")