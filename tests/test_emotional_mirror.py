import unittest
from core.emotional_mirror import EmotionalMirror

class TestEmotionalMirror(unittest.TestCase):
    def setUp(self):
        self.mirror = EmotionalMirror()

    def test_analyze_sentiment_positive(self):
        text = "I am so happy and excited today!"
        score = self.mirror.analyze_sentiment(text)
        self.assertGreater(score, 0)

    def test_analyze_sentiment_negative(self):
        text = "I am very sad and depressed."
        score = self.mirror.analyze_sentiment(text)
        self.assertLess(score, 0)

    def test_analyze_sentiment_neutral(self):
        text = "The table is made of wood."
        score = self.mirror.analyze_sentiment(text)
        # Neutral statements should be close to 0
        self.assertAlmostEqual(score, 0, delta=0.1)

    def test_analyze_sentiment_empty(self):
        text = ""
        score = self.mirror.analyze_sentiment(text)
        self.assertEqual(score, 0.0)

    def test_analyze_sentiment_none(self):
        text = None
        score = self.mirror.analyze_sentiment(text)
        self.assertEqual(score, 0.0)

    def test_generate_empathetic_response(self):
        # Test positive response
        response = self.mirror.generate_empathetic_response(0.8)
        self.assertIn("glad", response)

        # Test negative response
        response = self.mirror.generate_empathetic_response(-0.8)
        self.assertIn("sorry", response)

        # Test neutral response
        response = self.mirror.generate_empathetic_response(0.0)
        self.assertIn("understand", response)

if __name__ == '__main__':
    unittest.main()
