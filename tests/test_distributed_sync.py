import unittest
from unittest.mock import MagicMock
import asyncio
from core.distributed_sync import DistributedSync

class TestDistributedSync(unittest.TestCase):
    def setUp(self):
        self.mock_memory = MagicMock()
        self.mock_ethics = MagicMock()
        self.syncer = DistributedSync(
            peers=[],
            memory_nexus=self.mock_memory,
            ethical_engine=self.mock_ethics
        )

    def test_receive_memory(self):
        data = {
            "type": "memory",
            "payload": {
                "user_id": "user1",
                "key": "test_key",
                "value": "test_value"
            }
        }

        asyncio.run(self.syncer.receive(data))

        self.mock_memory.store_memory.assert_called_with("user1", "test_key", "test_value")

    def test_receive_ethics(self):
        data = {
            "type": "ethics",
            "payload": {
                "action": "harmful action"
            }
        }
        self.mock_ethics.evaluate_action.return_value = (False, "Unethical")

        result = asyncio.run(self.syncer.receive(data))

        self.mock_ethics.evaluate_action.assert_called_with("harmful action")
        self.assertEqual(result, {"result": (False, "Unethical")})

    def test_receive_unknown(self):
        data = {"type": "unknown", "payload": {}}
        result = asyncio.run(self.syncer.receive(data))
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
