from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config.db_config import get_db
from backend.services.user_management import create_user, get_user, get_users, delete_user

router = APIRouter()

@router.post("/")
def create_new_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)

@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.delete("/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
