from fastapi import FastAPI
from celery.result import AsyncResult
from app.tasks import celery_app

app = FastAPI()

@app.post("/add")
def run_task(x: int, y: int):
    """
    Endpoint to run a Celery task that adds two numbers.
    It sends the task to the Celery worker and returns the task ID.
    """
    task = celery_app.send_task("app.tasks.example_task", args=[x, y])
    return {"task_id": task.id}


@app.get("/status/{task_id}")
def get_status(task_id: str):
    """
    Endpoint to check the status of a Celery task.
    It retrieves the task status and result using the task ID.
    """
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result
    }
