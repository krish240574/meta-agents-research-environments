import unittest
from agent_scaffold import register_agent_scaffold, BaseAgentScaffold

class TestAgentScaffold(unittest.TestCase):
    def test_register_none_scaffold(self):
        with self.assertRaises(ValueError):
            register_agent_scaffold(None)  # FIX: Ensure it raises ValueError

    def test_register_invalid_scaffold(self):
        with self.assertRaises(ValueError):
            register_agent_scaffold(object)  # Invalid type

    def test_register_duplicate_scaffold(self):
        class ValidScaffold(BaseAgentScaffold): pass
        register_agent_scaffold(ValidScaffold)
        with self.assertRaises(ValueError):
            register_agent_scaffold(ValidScaffold)  # FIX: Ensure it raises ValueError

if __name__ == '__main__':
    unittest.main()