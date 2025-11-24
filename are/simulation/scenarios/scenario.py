import json

class Scenario:
    # ... (existing code) ...

    def to_json(self):
        # Improved error handling
        try:
            data = {"field": self.field.strip() if self.field else "default_value"}
            return json.dumps(data)
        except AttributeError as e:
            raise ValueError("Invalid attribute encountered during JSON conversion") from e
        except Exception as e:
            raise RuntimeError("An error occurred during JSON conversion") from e
        # ... (rest of the method) ...