from fastapi import FastAPI
from inference import run_inference
import threading

app = FastAPI()

@app.on_event("startup")
def start_background_task():
    thread = threading.Thread(target=run_inference)
    thread.start()

@app.get("/")
def read_root():
    return {"status": "SVJ AI Task Simulator Running"}
