from sqlalchemy.orm import Session
from app.models import Exercise, Workout, User
from app.schemas.exercise import ExerciseBase


def create_exercise(db: Session, workout_id: int, data: ExerciseBase, current_user: User):
    # 親workoutが「自分のもの」かチェック
    workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id, Workout.user_id == current_user.id)
        .first()
    )
    if workout is None:
        return None

    exercise = Exercise(workout_id=workout_id, name=data.name)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise


def update_exercise(db: Session, exercise_id: int, data: ExerciseBase, current_user: User):
    # Exercise -> Workout まで辿って所有者チェック
    exercise = (
        db.query(Exercise)
        .join(Workout, Exercise.workout_id == Workout.id)
        .filter(Exercise.id == exercise_id, Workout.user_id == current_user.id)
        .first()
    )
    if exercise is None:
        return None

    exercise.name = data.name
    db.commit()
    db.refresh(exercise)
    return exercise


def delete_exercise(db: Session, exercise_id: int, current_user: User):
    exercise = (
        db.query(Exercise)
        .join(Workout, Exercise.workout_id == Workout.id)
        .filter(Exercise.id == exercise_id, Workout.user_id == current_user.id)
        .first()
    )
    if exercise is None:
        return None

    db.delete(exercise)
    db.commit()
    return exercise
