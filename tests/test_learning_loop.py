import sys
import os
import unittest
import asyncio
import json
from unittest.mock import MagicMock
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.learning_loop import LearningLoop

class TestLearningLoop(unittest.IsolatedAsyncioTestCase):
    async def test_retrain_creates_snapshot(self):
        learning_loop = LearningLoop()
        learning_loop.memory.storage = {"key": "value"}
        result = await learning_loop.retrain()
        self.assertTrue(result.startswith("Snapshot saved:"))
        filepath = result.split(": ")[1]
        self.assertTrue(os.path.exists(filepath))
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, {"key": "value"})
        os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
