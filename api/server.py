from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from core.namo_ai import NamoAI
from core.distributed_sync import DistributedSync

namo_ai = NamoAI()
syncer = DistributedSync(peers=["https://namo-node2.run.app"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await syncer.close()

app = FastAPI(lifespan=lifespan)

class UserInput(BaseModel):
    user_id: str
    text: str

@app.post("/namo/interact")
def interact(user_input: UserInput):
    response = namo_ai.interact(user_input.user_id, user_input.text)
    return {"response": response}

@app.post("/namo/sync")
async def sync(data: dict):
    return {"status": "ok", "received": data}

@app.post("/namo/broadcast")
async def broadcast(data: dict):
    await syncer.broadcast(data)
    return {"status": "broadcasted", "peers": syncer.peers}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
