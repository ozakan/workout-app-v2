from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import workout, exercise, set

app = FastAPI()

# --- DBテーブル作成（初回起動時のみ） ---
Base.metadata.create_all(bind=engine)

# --- ルーター登録 ---
app.include_router(workout.router)
app.include_router(exercise.router)
app.include_router(set.router)
