from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import uuid
from src.constants import UI_URL, WORKER_URL
from src.models import WorkUnit

app = FastAPI()

origins = [
    str(UI_URL),
    str(WORKER_URL),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


# POST request to analyze content
@app.post("/submit")
def submit(request: WorkUnit):
    # Generate a unique socket ID
    socket = str(uuid.uuid4())

    # TODO: Notify the worker server with the analysis request
    request_url = WORKER_URL / "process"
    try:
        print({"socket": socket, "work": request.dict()})
        response = requests.post(
            request_url, json={"socket": socket, "work": request.dict()}
        )

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="No workers available")

    return {"socket": socket}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
