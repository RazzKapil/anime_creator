
from fastapi import APIRouter
from backend.tasks.video_pipeline import generate_video

router = APIRouter()

@router.post("/generate")
def start_generation(prompt: str, user_id: str):
    task = generate_video.delay(prompt, user_id)
    return {"task_id": task.id}
