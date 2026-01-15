from typing import List, Dict

class CollectiveMemory:
    def __init__(self):
        self.cluster_knowledge = []
        self.seen_inputs = set()

    async def aggregate(self, memories: List[Dict]):
        for m in memories:
            if m['input'] not in self.seen_inputs:
                self.seen_inputs.add(m['input'])
                self.cluster_knowledge.append(m)
        return len(self.cluster_knowledge)
