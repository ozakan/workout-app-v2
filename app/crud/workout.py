from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import Workout
from app.schemas.workout import WorkoutBase

def get_all_workouts(db: Session):
    return db.query(Workout).order_by(Workout.date.desc()).all()


def create_workout(db: Session, data: WorkoutBase):
    workout = Workout(date=data.date)
    db.add(workout)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        return None  # ← ここで「重複」として返す
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

def get_workout(db: Session, workout_id: int):
    return db.query(Workout).filter(Workout.id == workout_id).first()

