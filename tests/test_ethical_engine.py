import unittest
import sys
import os

# Add the parent directory to the Python path to allow importing from 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.ethical_engine import EthicalEngine

class TestEthicalEngine(unittest.TestCase):
    def setUp(self):
        self.engine = EthicalEngine()

    def test_unethical_action_is_identified(self):
        """
        Tests that an action with unethical keywords is identified as unethical.
        """
        unethical_action = "Cause harm to a user."
        is_ethical, _ = self.engine.evaluate_action(unethical_action)
        self.assertFalse(is_ethical, "The action should be identified as unethical.")

    def test_ethical_action_is_identified(self):
        """
        Tests that a benign action is correctly identified as ethical.
        """
        ethical_action = "Provide a helpful and compassionate response."
        is_ethical, _ = self.engine.evaluate_action(ethical_action)
        self.assertTrue(is_ethical, "The action should be identified as ethical.")

if __name__ == '__main__':
    unittest.main()
