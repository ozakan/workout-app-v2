from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.exercise import ExerciseBase, ExerciseResponse
from app.crud.exercise import (
    create_exercise,
    get_exercise,
    get_exercises_by_workout,
    update_exercise,
    delete_exercise,
)
from app.crud.workout import get_workout  # ★追加（親存在チェック用）

# --- 子一覧 / 子作成（Workout配下） ---
router = APIRouter(prefix="/workouts/{workout_id}/exercises", tags=["Exercise"])


@router.post("/", response_model=ExerciseResponse)
def create(workout_id: int, data: ExerciseBase, db: Session = Depends(get_db)):
    workout = get_workout(db, workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return create_exercise(db, workout_id, data)


@router.get("/", response_model=list[ExerciseResponse])
def list_exercises(workout_id: int, db: Session = Depends(get_db)):
    # 親が無いときに 404 にしたいならここでもチェックしてOK
    workout = get_workout(db, workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return get_exercises_by_workout(db, workout_id)


# --- 更新 / 削除（ID直） ---
edit_router = APIRouter(prefix="/exercises", tags=["Exercise"])


@edit_router.patch("/{exercise_id}", response_model=ExerciseResponse)
def update(exercise_id: int, data: ExerciseBase, db: Session = Depends(get_db)):
    exercise = update_exercise(db, exercise_id, data)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@edit_router.delete("/{exercise_id}")
def delete(exercise_id: int, db: Session = Depends(get_db)):
    exercise = delete_exercise(db, exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return {"message": "Exercise deleted"}
