from sqlalchemy.orm import Session
from app.models import Workout
from app.schemas.workout import WorkoutBase

def get_all_workouts(db: Session):
    return db.query(Workout).all()


def create_workout(db: Session, data: WorkoutBase):
    workout = Workout(date=data.date)
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

def get_workout_by_date(db: Session, date: str):
    return (
        db.query(Workout)
        .filter(Workout.date == date)
        .first()
    )

def update_workout(db: Session, workout_id: int, data: WorkoutBase):
    workout = db.query(Workout).filter(Workout.id == workout_id).first()
    if workout:
        workout.date = data.date
        db.commit()
        db.refresh(workout)
    return workout

def delete_workout(db: Session, workout_id: int):
    workout = db.query(Workout).filter(Workout.id == workout_id).first()
    if workout:
        db.delete(workout)
        db.commit()
    return workout
