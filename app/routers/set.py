from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.set import SetBase, SetResponse
from app.security import get_current_user
from app.models import User
from app.crud.set import (
    create_set,
    update_set,
    delete_set,
)

# 作成（Exercise配下）
router = APIRouter(prefix="/exercises/{exercise_id}/sets", tags=["Set"])


@router.post("/", response_model=SetResponse)
def create(
    exercise_id: int,
    data: SetBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = create_set(db, exercise_id, data, current_user)
    if item is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return item


# 更新/削除（ID直）
edit_router = APIRouter(prefix="/sets", tags=["Set"])


@edit_router.patch("/{set_id}", response_model=SetResponse)
def update(
    set_id: int,
    data: SetBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = update_set(db, set_id, data, current_user)
    if item is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return item


@edit_router.delete("/{set_id}")
def delete(
    set_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = delete_set(db, set_id, current_user)
    if item is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"message": "Set deleted"}
