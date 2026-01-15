import aiohttp, asyncio, json
from typing import Dict, List, Optional

class DistributedSync:
    def __init__(self, peers: List[str]):
        self.peers = peers
        self.session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def _send(self, url: str, payload: Dict):
        session = await self._get_session()
        async with session.post(url, json=payload) as response:
            await response.read()

    async def broadcast(self, payload: Dict):
        tasks = [self._send(f"{p}/namo/sync", payload) for p in self.peers]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()

    async def receive(self, data: Dict):
        print("📡 Received sync:", json.dumps(data, ensure_ascii=False))
        # จะโยนต่อให้ memory หรือ ethics ประมวลผล
