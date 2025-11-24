import json

class Scenario:
    def __init__(self, name, agents, parameters):
        self.name = name
        self.agents = agents
        self.parameters = parameters

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'agents': self.agents,
            'parameters': self.parameters
        })
