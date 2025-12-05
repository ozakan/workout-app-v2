from sqlalchemy.orm import Session
from app.models import Set
from app.schemas.set import SetBase

def create_set(db: Session, exercise_id: int, data: SetBase):
    set_item = Set(exercise_id=exercise_id, weight=data.weight, reps=data.reps)
    db.add(set_item)
    db.commit()
    db.refresh(set_item)
    return set_item

def get_sets_by_exercise(db: Session, exercise_id: int):
    return db.query(Set).filter(Set.exercise_id == exercise_id).all()

def update_set(db: Session, set_id: int, data: SetBase):
    set_item = db.query(Set).filter(Set.id == set_id).first()
    if set_item:
        set_item.weight = data.weight
        set_item.reps = data.reps
        db.commit()
        db.refresh(set_item)
    return set_item

def delete_set(db: Session, set_id: int):
    set_item = db.query(Set).filter(Set.id == set_id).first()
    if set_item:
        db.delete(set_item)
        db.commit()
    return set_item
