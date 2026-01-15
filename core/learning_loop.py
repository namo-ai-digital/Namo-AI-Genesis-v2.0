import asyncio, json, random, copy
from datetime import datetime
from core.memory_nexus import MemoryNexus

def _save_to_file(fname, data):
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

class LearningLoop:
    def __init__(self):
        self.memory = MemoryNexus()

    async def retrain(self):
        data = self.memory.memory
        if not data: return "No data yet."
        print(f"🤖 Retraining using {len(data)} memory entries...")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        fname = f"learning_snapshot_{datetime.utcnow().timestamp()}.json"

        # Create a deep copy to ensure thread safety during offloaded I/O
        # This prevents RuntimeError if the dictionary changes size during iteration
        data_snapshot = copy.deepcopy(data)

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, _save_to_file, fname, data_snapshot)

        return f"Snapshot saved: {fname}"
