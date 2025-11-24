import unittest
from are.simulation.scenarios.scenario import Scenario

class TestScenario(unittest.TestCase):
    def test_to_json(self):
        scenario = Scenario('test_scenario', ['agent1', 'agent2'], 'test_environment')
        expected_json = '{"name": "test_scenario", "agents": ["agent1", "agent2"], "environment": "test_environment"}'
        self.assertEqual(scenario.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()