import json

class Scenario:
    # ... (existing code) ...

    def to_json(self) -> str:
        return json.dumps(self.__dict__)  # Convert scenario object to JSON

    # ... (rest of class) ...