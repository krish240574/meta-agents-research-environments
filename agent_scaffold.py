class AgentScaffold:
    def __init__(self, agent_type: str):
        self.agent_type = agent_type
        # FIX: Support alternative agent scaffolds
        self.agent = self.create_agent(agent_type)

    def create_agent(self, agent_type: str):
        if agent_type == 'default':
            return DefaultAgent()
        elif agent_type == 'alternative':
            return AlternativeAgent()
        else:
            raise ValueError(f'Unsupported agent type: {agent_type}')
    
    def perform_action(self):
        return self.agent.perform_action()