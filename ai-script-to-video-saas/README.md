
# AI Script-to-Video SaaS

Full-stack project using FastAPI + Celery + Redis (backend) and Next.js (frontend).

## How to Run in GitHub Codespaces

1. Open repo in Codespaces
2. Backend:
```bash
uvicorn backend.main:app --reload --port 8000
```
3. Worker:
```bash
celery -A worker.celery_worker worker --loglevel=info
```
4. Frontend:
```bash
cd frontend
npm install
npm run dev
```

Then open frontend on http://localhost:3000 and backend docs at http://localhost:8000/docs
