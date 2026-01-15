import aiohttp, asyncio, json
from typing import Dict, List

class DistributedSync:
    def __init__(self, peers: List[str], memory_nexus=None, ethical_engine=None):
        self.peers = peers
        self.memory_nexus = memory_nexus
        self.ethical_engine = ethical_engine

    async def broadcast(self, payload: Dict):
        async with aiohttp.ClientSession() as s:
            tasks = [s.post(f"{p}/namo/sync", json=payload) for p in self.peers]
            await asyncio.gather(*tasks, return_exceptions=True)

    async def receive(self, data: Dict):
        print("📡 Received sync:", json.dumps(data, ensure_ascii=False))

        sync_type = data.get("type")
        payload = data.get("payload", {})

        if sync_type == "memory" and self.memory_nexus:
            user_id = payload.get("user_id")
            key = payload.get("key")
            value = payload.get("value")
            if user_id and key and value:
                self.memory_nexus.store_memory(user_id, key, value)
                return {"status": "stored", "key": key}

        elif sync_type == "ethics" and self.ethical_engine:
            action = payload.get("action")
            if action:
                is_ethical, justification = self.ethical_engine.evaluate_action(action)
                return {"result": (is_ethical, justification)}

        return None
