from fastapi import FastAPI, HTTPException
import requests
import uuid

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# POST request to analyze content
@app.post("/submit")
def submit(request):
    # Generate a unique socket ID
    socket_id = str(uuid.uuid4())

    # Notify the worker server with the analysis request
    worker_url = "http://localhost:8001/process"
    response = requests.post(
        worker_url, json={"socket_id": socket_id, "request": request.dict()}
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Failed to notify the worker server"
        )

    return {"socket_id": socket_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
