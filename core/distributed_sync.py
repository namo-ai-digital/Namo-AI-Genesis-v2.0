import aiohttp, asyncio, json
from typing import Dict, List

class DistributedSync:
    def __init__(self, peers: List[str]):
        self.peers = peers

    async def broadcast(self, payload: Dict):
        async with aiohttp.ClientSession() as s:
            tasks = [s.post(f"{p}/namo/sync", json=payload) for p in self.peers]
            await asyncio.gather(*tasks, return_exceptions=True)

    async def receive(self, data: Dict):
        print("📡 Received sync:", json.dumps(data, ensure_ascii=False))
        # จะโยนต่อให้ memory หรือ ethics ประมวลผล
