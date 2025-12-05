from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.exercise import ExerciseBase, ExerciseResponse
from app.crud.exercise import (
    create_exercise,
    get_exercise,
    get_exercises_by_workout,
    update_exercise,
    delete_exercise
)

router = APIRouter(prefix="/exercises", tags=["Exercise"])


@router.post("/{workout_id}", response_model=ExerciseResponse)
def create(workout_id: int, data: ExerciseBase, db: Session = Depends(get_db)):
    return create_exercise(db, workout_id, data)


@router.get("/{workout_id}", response_model=list[ExerciseResponse])
def list_exercises(workout_id: int, db: Session = Depends(get_db)):
    return get_exercises_by_workout(db, workout_id)


@router.patch("/{exercise_id}", response_model=ExerciseResponse)
def update(exercise_id: int, data: ExerciseBase, db: Session = Depends(get_db)):
    exercise = update_exercise(db, exercise_id, data)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@router.delete("/{exercise_id}")
def delete(exercise_id: int, db: Session = Depends(get_db)):
    exercise = delete_exercise(db, exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return {"message": "Exercise deleted"}
