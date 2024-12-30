from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.services.authentication import authenticate_user, create_access_token
from backend.config.db_config import get_db

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
