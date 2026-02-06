from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.exercise import ExerciseBase, ExerciseResponse
from app.security import get_current_user
from app.models import User
from app.crud.exercise import (
    create_exercise,
    update_exercise,
    delete_exercise,
)

# 作成（Workout配下）
router = APIRouter(prefix="/workouts/{workout_id}/exercises", tags=["Exercise"])


@router.post("/", response_model=ExerciseResponse)
def create(
    workout_id: int,
    data: ExerciseBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    exercise = create_exercise(db, workout_id, data, current_user)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return exercise


# 更新/削除（ID直）
edit_router = APIRouter(prefix="/exercises", tags=["Exercise"])


@edit_router.patch("/{exercise_id}", response_model=ExerciseResponse)
def update(
    exercise_id: int,
    data: ExerciseBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    exercise = update_exercise(db, exercise_id, data, current_user)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@edit_router.delete("/{exercise_id}")
def delete(
    exercise_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    exercise = delete_exercise(db, exercise_id, current_user)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return {"message": "Exercise deleted"}
