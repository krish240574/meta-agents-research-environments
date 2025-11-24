import json

class Scenario:
    # ... (existing attributes and methods) ...

    def to_json(self) -> str:
        return json.dumps(self.__dict__)  # Convert scenario attributes to JSON
