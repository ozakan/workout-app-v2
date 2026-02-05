from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.workout import WorkoutBase, WorkoutResponse
from app.crud.workout import (
    get_all_workouts,
    create_workout,
    get_workout_by_date,
    update_workout,
    delete_workout,
    get_workout
)

router = APIRouter(prefix="/workouts", tags=["Workout"])


@router.post("/", response_model=WorkoutResponse)
def create(data: WorkoutBase, db: Session = Depends(get_db)):
    workout = create_workout(db, data)
    if workout is None:
        raise HTTPException(status_code=409, detail="Workout date already exists")
    return workout

@router.get("/", response_model=list[WorkoutResponse])
def list_workouts(db: Session = Depends(get_db)):
    return get_all_workouts(db)

@router.get("/{workout_id}", response_model=WorkoutResponse)
def get_by_id(workout_id: int, db: Session = Depends(get_db)):
    workout = get_workout(db, workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout



@router.get("/{date}", response_model=WorkoutResponse)
def get(date: str, db: Session = Depends(get_db)):
    workout = get_workout_by_date(db, date)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


@router.patch("/{workout_id}", response_model=WorkoutResponse)
def update(workout_id: int, data: WorkoutBase, db: Session = Depends(get_db)):
    workout = update_workout(db, workout_id, data)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


@router.delete("/{workout_id}")
def delete(workout_id: int, db: Session = Depends(get_db)):
    workout = delete_workout(db, workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return {"message": "Workout deleted"}
