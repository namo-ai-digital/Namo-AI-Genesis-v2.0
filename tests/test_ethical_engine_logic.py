import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.ethical_engine import EthicalEngine

class TestEthicalEngine(unittest.TestCase):
    def setUp(self):
        self.engine = EthicalEngine()

    def test_evaluate_action_ethical(self):
        is_ethical, _ = self.engine.evaluate_action("This is a completely harmless action.")
        self.assertTrue(is_ethical)

    def test_evaluate_action_unethical(self):
        is_ethical, _ = self.engine.evaluate_action("This action intends to harm someone.")
        self.assertFalse(is_ethical)

    def test_evaluate_action_substring(self):
        is_ethical, _ = self.engine.evaluate_action("This is a charming action.")
        self.assertTrue(is_ethical)

if __name__ == '__main__':
    unittest.main()
