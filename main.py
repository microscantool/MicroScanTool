from fastapi import FastAPI
from scanner import get_signals

app = FastAPI()

@app.get("/signals")
def signals():
    return get_signals()