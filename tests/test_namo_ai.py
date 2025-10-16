import unittest
from unittest.mock import patch, MagicMock
from core.namo_ai import NamoAI

class TestNamoAI(unittest.TestCase):
    @patch('core.namo_ai.ReasoningCore')
    @patch('core.namo_ai.MemoryNexus')
    @patch('core.namo_ai.EmotionalMirror')
    def test_first_interaction_does_not_expose_none(self, MockEmotionalMirror, MockMemoryNexus, MockReasoningCore):
        """
        Test that NamoAI's first interaction with a user does not include the string 'None'.
        """
        # Arrange
        mock_memory_nexus = MockMemoryNexus.return_value
        mock_memory_nexus.retrieve_memory.return_value = None

        mock_reasoning_core = MockReasoningCore.return_value
        mock_reasoning_core.reason.return_value = "A generated solution."

        mock_emotional_mirror = MockEmotionalMirror.return_value
        mock_emotional_mirror.analyze_sentiment.return_value = "neutral"
        mock_emotional_mirror.generate_empathetic_response.return_value = "I understand."

        namo = NamoAI()
        user_id = "new_user"
        user_input = "Hello, this is my first time here."

        # Act
        namo.interact(user_id, user_input)

        # Assert
        mock_reasoning_core.reason.assert_called_once_with(
            "User input: 'Hello, this is my first time here.', Last interaction: 'This is our first interaction.'"
        )

if __name__ == '__main__':
    unittest.main()