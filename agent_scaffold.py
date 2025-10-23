class AgentScaffold:
    def __init__(self, agent_type: str):
        self.agent_type = agent_type
        self.validate_agent_type()  # FIX: Validate agent type

    def validate_agent_type(self):
        valid_agents = ['react', 'custom']  # Example valid agents
        if self.agent_type not in valid_agents:
            raise ValueError(f"Unsupported agent type: {self.agent_type}")

    # ... (other methods) ...