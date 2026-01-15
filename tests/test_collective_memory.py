import unittest
import asyncio
from core.collective_memory import CollectiveMemory

class TestCollectiveMemory(unittest.TestCase):
    def setUp(self):
        self.cm = CollectiveMemory()

    def test_aggregate_adds_memories(self):
        memories = [{'input': 'a'}, {'input': 'b'}]
        asyncio.run(self.cm.aggregate(memories))
        self.assertEqual(len(self.cm.cluster_knowledge), 2)
        self.assertEqual(self.cm.cluster_knowledge[0]['input'], 'a')
        self.assertEqual(self.cm.cluster_knowledge[1]['input'], 'b')

    def test_aggregate_deduplicates_within_batch(self):
        memories = [{'input': 'a'}, {'input': 'a'}, {'input': 'b'}]
        asyncio.run(self.cm.aggregate(memories))
        self.assertEqual(len(self.cm.cluster_knowledge), 2)
        inputs = [m['input'] for m in self.cm.cluster_knowledge]
        self.assertIn('a', inputs)
        self.assertIn('b', inputs)

    def test_aggregate_deduplicates_across_batches(self):
        memories1 = [{'input': 'a'}]
        asyncio.run(self.cm.aggregate(memories1))

        memories2 = [{'input': 'a'}, {'input': 'b'}]
        asyncio.run(self.cm.aggregate(memories2))

        self.assertEqual(len(self.cm.cluster_knowledge), 2)
        inputs = [m['input'] for m in self.cm.cluster_knowledge]
        self.assertIn('a', inputs)
        self.assertIn('b', inputs)

if __name__ == '__main__':
    unittest.main()
