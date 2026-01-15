from fastapi import FastAPI
from pydantic import BaseModel
from core.namo_ai import NamoAI
from core.distributed_sync import DistributedSync

app = FastAPI()
namo_ai = NamoAI()
syncer = DistributedSync(
    peers=["https://namo-node2.run.app"],
    memory_nexus=namo_ai.memory_nexus,
    ethical_engine=namo_ai.ethical_engine
)

class UserInput(BaseModel):
    user_id: str
    text: str

@app.post("/namo/interact")
def interact(user_input: UserInput):
    response = namo_ai.interact(user_input.user_id, user_input.text)
    return {"response": response}

@app.post("/namo/sync")
async def sync(data: dict):
    result = await syncer.receive(data)
    return {"status": "ok", "received": data, "processed_result": result}

@app.post("/namo/broadcast")
async def broadcast(data: dict):
    await syncer.broadcast(data)
    return {"status": "broadcasted", "peers": syncer.peers}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
