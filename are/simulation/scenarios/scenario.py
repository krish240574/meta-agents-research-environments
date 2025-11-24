import json

class Scenario:
    def __init__(self, name, agents, actions):
        self.name = name
        self.agents = agents
        self.actions = actions

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'agents': self.agents,
            'actions': self.actions
        })