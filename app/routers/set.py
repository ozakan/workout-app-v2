from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.set import SetBase, SetResponse
from app.crud.set import (
    create_set,
    get_sets_by_exercise,
    update_set,
    delete_set,
)
from app.crud.exercise import get_exercise  # ★追加（親存在チェック用）

# --- 子一覧 / 子作成（Exercise配下） ---
router = APIRouter(prefix="/exercises/{exercise_id}/sets", tags=["Set"])


@router.post("/", response_model=SetResponse)
def create(exercise_id: int, data: SetBase, db: Session = Depends(get_db)):
    exercise = get_exercise(db, exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return create_set(db, exercise_id, data)


@router.get("/", response_model=list[SetResponse])
def list_sets(exercise_id: int, db: Session = Depends(get_db)):
    exercise = get_exercise(db, exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return get_sets_by_exercise(db, exercise_id)


# --- 更新 / 削除（ID直） ---
edit_router = APIRouter(prefix="/sets", tags=["Set"])


@edit_router.patch("/{set_id}", response_model=SetResponse)
def update(set_id: int, data: SetBase, db: Session = Depends(get_db)):
    item = update_set(db, set_id, data)
    if item is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return item


@edit_router.delete("/{set_id}")
def delete(set_id: int, db: Session = Depends(get_db)):
    item = delete_set(db, set_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"message": "Set deleted"}
