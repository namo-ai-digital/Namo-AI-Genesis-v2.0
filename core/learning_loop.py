import asyncio, json, random
from datetime import datetime
from core.memory_nexus import MemoryNexus

class LearningLoop:
    def __init__(self):
        self.memory = MemoryNexus()

    async def retrain(self):
        data = self.memory.storage
        if not data: return "No data yet."
        print(f"🤖 Retraining using {len(data)} memory entries...")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        fname = f"learning_snapshot_{datetime.utcnow().timestamp()}.json"
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return f"Snapshot saved: {fname}"
