import unittest
import asyncio
from unittest.mock import patch, MagicMock, AsyncMock, PropertyMock
from core.distributed_sync import DistributedSync

class TestDistributedSync(unittest.TestCase):
    def test_broadcast(self):
        async def run_test():
            peers = ["http://peer1", "http://peer2"]
            syncer = DistributedSync(peers)
            payload = {"key": "value"}

            # patch aiohttp.ClientSession
            with patch('aiohttp.ClientSession') as MockSessionClass:
                mock_session = MockSessionClass.return_value

                # Ensure close is awaitable
                mock_session.close = AsyncMock()
                # Ensure closed property is False
                type(mock_session).closed = PropertyMock(return_value=False)

                # Mock response object
                mock_response = AsyncMock()
                mock_response.read = AsyncMock(return_value=b"ok")

                # Mock post context manager
                mock_post_ctx = MagicMock()
                mock_post_ctx.__aenter__ = AsyncMock(return_value=mock_response)
                mock_post_ctx.__aexit__ = AsyncMock(return_value=None)

                # session.post() returns the context manager
                mock_session.post.return_value = mock_post_ctx

                await syncer.broadcast(payload)

                self.assertEqual(mock_session.post.call_count, 2)
                calls = mock_session.post.call_args_list
                urls = [c[0][0] for c in calls]
                self.assertIn("http://peer1/namo/sync", urls)
                self.assertIn("http://peer2/namo/sync", urls)

                # Verify clean up
                await syncer.close()
                mock_session.close.assert_called_once()

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_test())
        loop.close()

if __name__ == '__main__':
    unittest.main()
