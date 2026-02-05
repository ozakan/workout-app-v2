from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import workout, exercise, set
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def root():
    return FileResponse("static/index.html")
# --- DBテーブル作成（初回起動時のみ） ---
Base.metadata.create_all(bind=engine)

# --- ルーター登録 ---
app.include_router(workout.router)
app.include_router(exercise.router)
app.include_router(exercise.edit_router)
app.include_router(set.router)
app.include_router(set.edit_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for r in app.routes:
    if hasattr(r, "methods"):
        print(r.path, r.methods)
