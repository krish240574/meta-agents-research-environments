import json

class Scenario:
    def __init__(self, name, agents, environment):
        self.name = name
        self.agents = agents
        self.environment = environment

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'agents': self.agents,
            'environment': self.environment
        })