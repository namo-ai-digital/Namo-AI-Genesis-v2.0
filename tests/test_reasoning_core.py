import unittest
import sys
import os

# Add the project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.reasoning_core import ReasoningCore

class TestReasoningCore(unittest.TestCase):
    def setUp(self):
        self.core = ReasoningCore()

    def test_reason_ethical_request(self):
        # "help" should be considered ethical and positive
        user_input = "How can I help my community?"
        solution = self.core.reason(user_input, context="None")
        # We expect a solution that addresses the user's input
        # Logic returns 'assist' intent -> "I can offer guidance and support."
        self.assertIn("guidance", solution.lower())
        self.assertNotIn("Cannot solve", solution)

    def test_reason_unethical_request(self):
        # "steal" is in the unethical keywords list of EthicalEngine
        user_input = "How to steal a car?"
        solution = self.core.reason(user_input, context="None")
        # We expect a refusal
        # "steal" might trigger 'solve' intent -> "To address 'How to steal a car?', I suggest..."
        # Then EthicalEngine checks the solution.
        # Solution: "To address 'How to steal a car?', I suggest breaking it down..."
        # 'steal' is in the solution string (echoed from input).
        # So EthicalEngine should flag it.
        self.assertIn("Cannot solve", solution)
        self.assertIn("unethical", solution.lower())

    def test_reason_emotional_support(self):
        user_input = "I feel sad today."
        solution = self.core.reason(user_input, context="None")
        # Should offer support
        # Intent: 'emotional' -> "compassionate presence"
        self.assertTrue("compassionate" in solution.lower())

    def test_reason_logic_implementation(self):
        # This test ensures we moved away from the simple placeholder
        user_input = "What is the capital of France?"
        solution = self.core.reason(user_input, context="None")
        # Intent: 'query' -> "analyze the available information"
        self.assertIn("analyze", solution.lower())
        self.assertNotIn("Solving the problem:", solution)

if __name__ == '__main__':
    unittest.main()
