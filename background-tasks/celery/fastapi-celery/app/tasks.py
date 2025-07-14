from celery import Celery

# Celery Setup with Redis as broker and backend
celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task(name="app.tasks.example_task")
def example_task(x: int, y: int) -> int:
    return x + y