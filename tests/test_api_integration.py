import unittest
from fastapi.testclient import TestClient
from api.server import app

class TestApiIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_sync_endpoint_memory(self):
        data = {
            "type": "memory",
            "payload": {
                "user_id": "api_user",
                "key": "api_key",
                "value": "api_value"
            }
        }
        response = self.client.post("/namo/sync", json=data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response["status"], "ok")
        self.assertEqual(json_response["processed_result"], {"status": "stored", "key": "api_key"})

    def test_sync_endpoint_ethics(self):
        data = {
            "type": "ethics",
            "payload": {
                "action": "do harm"
            }
        }
        response = self.client.post("/namo/sync", json=data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn("processed_result", json_response)
        # Check if result contains the evaluation (False because "harmful" matches "harm")
        result = json_response["processed_result"]
        self.assertIsNotNone(result)
        self.assertIn("result", result)
        is_ethical, justification = result["result"]
        self.assertFalse(is_ethical)

if __name__ == '__main__':
    unittest.main()
