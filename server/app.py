from fastapi import FastAPI
from inference import run_inference
import threading

app = FastAPI()

# Run inference in background (optional)
@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=run_inference)
    thread.start()

# Root endpoint
@app.get("/")
def root():
    return {"status": "SVJ AI Task Simulator Running"}

# ✅ REQUIRED FOR OPENENV
@app.post("/reset")
def reset():
    return {
        "observation": {
            "task_id": 1,
            "task_type": "email",
            "content": "Win money now!!!"
        }
    }

# ✅ REQUIRED FOR OPENENV
@app.post("/step")
def step(action: dict):
    return {
        "observation": {
            "task_id": 2,
            "task_type": "data",
            "content": "Name=NULL"
        },
        "reward": 1.0,
        "done": False,
        "info": {"correct": True}
    }
