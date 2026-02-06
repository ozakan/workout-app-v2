from sqlalchemy.orm import Session
from app.models import Workout, User
from app.schemas.workout import WorkoutBase


def get_all_workouts(db: Session, current_user: User):
    return (
        db.query(Workout)
        .filter(Workout.user_id == current_user.id)
        .order_by(Workout.date.desc())
        .all()
    )


def get_workout(db: Session, workout_id: int, current_user: User):
    # 自分のworkoutだけ取得できる
    return (
        db.query(Workout)
        .filter(
            Workout.id == workout_id,
            Workout.user_id == current_user.id,
        )
        .first()
    )


def create_workout(db: Session, data: WorkoutBase, current_user: User):
    # 同じユーザーで同じ日付があるかチェック
    existing = (
        db.query(Workout)
        .filter(
            Workout.user_id == current_user.id,
            Workout.date == data.date
        )
        .first()
    )
    if existing:
        return None

    workout = Workout(date=data.date, user_id=current_user.id)
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout


def delete_workout(db: Session, workout_id: int, current_user: User):
    # 自分のworkoutだけ削除できる
    workout = get_workout(db, workout_id, current_user)
    if workout:
        db.delete(workout)
        db.commit()
    return workout
