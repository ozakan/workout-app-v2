from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.workout import WorkoutBase, WorkoutResponse
from app.security import get_current_user
from app.models import User
from app.crud.workout import (
    get_all_workouts,
    create_workout,
    delete_workout,
    get_workout,
)

router = APIRouter(prefix="/workouts", tags=["Workout"])


@router.post("/", response_model=WorkoutResponse)
def create(
    data: WorkoutBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    workout = create_workout(db, data, current_user)
    if workout is None:
        raise HTTPException(status_code=409, detail="Workout date already exists")
    return workout


@router.get("/", response_model=list[WorkoutResponse])
def list_workouts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_workouts(db, current_user)


@router.get("/{workout_id}", response_model=WorkoutResponse)
def get_by_id(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    workout = get_workout(db, workout_id, current_user)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


@router.delete("/{workout_id}")
def delete(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    workout = delete_workout(db, workout_id, current_user)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return {"message": "Workout deleted"}
