
from worker.celery_worker import celery

@celery.task
def generate_video(prompt, user_id):
    print(f"Generating video for: {prompt} (User: {user_id})")
    return "video_generated.mp4"
