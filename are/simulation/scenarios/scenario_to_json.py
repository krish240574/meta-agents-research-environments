import json

class Scenario:
    def __init__(self, name, agents, parameters):
        self.name = name
        self.agents = agents
        self.parameters = parameters

    def to_json(self):
        # Convert scenario to JSON format
        scenario_dict = {
            'name': self.name,
            'agents': self.agents,
            'parameters': self.parameters
        }
        return json.dumps(scenario_dict)
