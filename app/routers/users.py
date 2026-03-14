from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, UTC
from typing import List

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.utils.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def add_user(data: UserCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(data.password_hash)

    user = User(
        name=data.name,
        username=data.username,
        email=data.email,
        password_hash=hashed_password
    )

    db.add(user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email déjà utilisé"
        )

    db.refresh(user)

    return user

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.deleted_at.is_(None)).all()
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) :
    user = db.query(User).filter(User.id == user_id, User.deleted_at.is_(None)).first()
    if not user :
        raise HTTPException(status_code=404, detail="User introuvable")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User introuvable")

    update_fields = data.model_dump(exclude_unset=True)

    if "password_hash" in update_fields:
        user.password_hash = hash_password(update_fields["password_hash"])
        update_fields.pop("password_hash")

    for key, value in update_fields.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User introuvable")

    if user.deleted_at is not None:
        raise HTTPException(status_code=400, detail="User déjà supprimé")

    user.deleted_at = datetime.now(UTC)

    db.commit()

    return {"message": "User supprimé avec succès"}