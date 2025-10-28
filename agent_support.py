class AlternativeAgent:
    def __init__(self, agent_type: str):
        self.agent_type = agent_type

    def execute(self, action: str):
        # Implement API call to the specific agent scaffold
        pass

# Function to register the alternative agent

def register_alternative_agent(agent_type: str) -> AlternativeAgent:
    return AlternativeAgent(agent_type)

# Example usage
# agent = register_alternative_agent('chatgpt')
# agent.execute('some_action')