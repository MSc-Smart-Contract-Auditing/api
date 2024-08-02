from fastapi import FastAPI, HTTPException
import requests
import uuid
from constants import WORKER_URL
from models import SubmitRequest

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# POST request to analyze content
@app.post("/submit")
def submit(request: SubmitRequest):
    # Generate a unique socket ID
    socket_id = str(uuid.uuid4())

    # Notify the worker server with the analysis request
    request_url = WORKER_URL / "process"
    try:
        response = requests.post(
            request_url, json={"socket_id": socket_id, "request": request.dict()}
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="No workers available")

    return {"socket_id": socket_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
