import json

class Scenario:
    def __init__(self, name, description, steps):
        self.name = name
        self.description = description
        self.steps = steps

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'description': self.description,
            'steps': self.steps
        })