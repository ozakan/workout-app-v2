from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.set import SetBase, SetResponse
from app.crud.set import (
    create_set,
    get_sets_by_exercise,
    update_set,
    delete_set
)

router = APIRouter(prefix="/sets", tags=["Set"])


@router.post("/{exercise_id}", response_model=SetResponse)
def create(exercise_id: int, data: SetBase, db: Session = Depends(get_db)):
    return create_set(db, exercise_id, data)


@router.get("/{exercise_id}", response_model=list[SetResponse])
def list_sets(exercise_id: int, db: Session = Depends(get_db)):
    return get_sets_by_exercise(db, exercise_id)


@router.patch("/{set_id}", response_model=SetResponse)
def update(set_id: int, data: SetBase, db: Session = Depends(get_db)):
    item = update_set(db, set_id, data)
    if item is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return item


@router.delete("/{set_id}")
def delete(set_id: int, db: Session = Depends(get_db)):
    item = delete_set(db, set_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"message": "Set deleted"}
