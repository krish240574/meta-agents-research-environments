import json

class Scenario:
    # ... (existing code) ...

    def to_json(self):
        # Converts scenario attributes to a JSON serializable format
        return json.dumps(self.__dict__)

    # ... (rest of class) ...