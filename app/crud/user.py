from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate
from app.security import hash_password


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)

    db_user = User(
        username=user.username,
        hashed_password=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
