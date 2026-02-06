from sqlalchemy.orm import Session
from app.models import Set, Exercise, Workout, User
from app.schemas.set import SetBase


def create_set(db: Session, exercise_id: int, data: SetBase, current_user: User):
    # Setの親の親（Workout）まで辿って所有者チェック
    ex = (
        db.query(Exercise)
        .join(Workout, Exercise.workout_id == Workout.id)
        .filter(Exercise.id == exercise_id, Workout.user_id == current_user.id)
        .first()
    )
    if ex is None:
        return None

    set_item = Set(exercise_id=exercise_id, weight=data.weight, reps=data.reps)
    db.add(set_item)
    db.commit()
    db.refresh(set_item)
    return set_item


def update_set(db: Session, set_id: int, data: SetBase, current_user: User):
    s = (
        db.query(Set)
        .join(Exercise, Set.exercise_id == Exercise.id)
        .join(Workout, Exercise.workout_id == Workout.id)
        .filter(Set.id == set_id, Workout.user_id == current_user.id)
        .first()
    )
    if s is None:
        return None

    s.weight = data.weight
    s.reps = data.reps
    db.commit()
    db.refresh(s)
    return s


def delete_set(db: Session, set_id: int, current_user: User):
    s = (
        db.query(Set)
        .join(Exercise, Set.exercise_id == Exercise.id)
        .join(Workout, Exercise.workout_id == Workout.id)
        .filter(Set.id == set_id, Workout.user_id == current_user.id)
        .first()
    )
    if s is None:
        return None

    db.delete(s)
    db.commit()
    return s
