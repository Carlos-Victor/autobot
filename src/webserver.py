import uvicorn

from fastapi import FastAPI
from threading import Thread

app = FastAPI()

@app.route("/")
def healthcheck():
    return {"status": True}

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def server():
    th = Thread(target=run)
    th.start()
