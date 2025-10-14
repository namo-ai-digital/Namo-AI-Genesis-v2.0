from typing import List, Dict

class CollectiveMemory:
    def __init__(self):
        self.cluster_knowledge = []

    async def aggregate(self, memories: List[Dict]):
        self.cluster_knowledge.extend(memories)
        # รวมและตัดซ้ำ
        seen = set()
        self.cluster_knowledge = [m for m in self.cluster_knowledge if not (m['input'] in seen or seen.add(m['input']))]
        return len(self.cluster_knowledge)
