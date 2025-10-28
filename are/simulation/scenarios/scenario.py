import json

class Scenario:
    # ... (existing code) ...

    def to_json(self):
        return json.dumps(self.__dict__)  # FIX: Convert scenario object to JSON

    # ... (rest of class) ...