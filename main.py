# main.py
from fastapi import FastAPI
from scanner import get_signals

app = FastAPI()

@app.get("/signals")  # THIS defines the /signals URL
def signals():
    return get_signals()