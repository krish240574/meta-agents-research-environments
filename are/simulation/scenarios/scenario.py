import json

class Scenario:
    # ... (existing attributes and methods) ...

    def to_json(self):
        return json.dumps(self.__dict__)  # Convert scenario attributes to JSON
