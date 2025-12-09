from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import workout, exercise, set
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- DBテーブル作成（初回起動時のみ） ---
Base.metadata.create_all(bind=engine)

# --- ルーター登録 ---
app.include_router(workout.router)
app.include_router(exercise.router)
app.include_router(set.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
