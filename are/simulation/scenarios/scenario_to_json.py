import json

class Scenario:
    def __init__(self, name, agents, parameters):
        self.name = name
        self.agents = agents
        self.parameters = parameters

    def to_json(self):
        # Convert scenario to JSON format
        scenario_dict = {
            'name': self.name if self.name is not None else '',
            'agents': self.agents if self.agents is not None else [],
            'parameters': self.parameters if self.parameters is not None else {}
        }
        return json.dumps(scenario_dict)
