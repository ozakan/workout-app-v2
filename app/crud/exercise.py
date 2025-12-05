from sqlalchemy.orm import Session
from app.models import Exercise
from app.schemas.exercise import ExerciseBase

def create_exercise(db: Session, workout_id: int, data: ExerciseBase):
    exercise = Exercise(workout_id=workout_id, name=data.name)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise

def get_exercise(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()

def get_exercises_by_workout(db: Session, workout_id: int):
    return db.query(Exercise).filter(Exercise.workout_id == workout_id).all()

def update_exercise(db: Session, exercise_id: int, data: ExerciseBase):
    exercise = get_exercise(db, exercise_id)
    if exercise:
        exercise.name = data.name
        db.commit()
        db.refresh(exercise)
    return exercise

def delete_exercise(db: Session, exercise_id: int):
    exercise = get_exercise(db, exercise_id)
    if exercise:
        db.delete(exercise)
        db.commit()
    return exercise
