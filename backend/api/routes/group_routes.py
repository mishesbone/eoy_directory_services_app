from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config.db_config import get_db
from backend.api.services.group_management import GroupManagementService
from backend.api.schemas.group_schema import GroupCreate, GroupResponse

router = APIRouter(prefix="/groups", tags=["Groups"])

@router.post("/", response_model=GroupResponse)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    try:
        return GroupManagementService.create_group(db, group)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{group_id}", response_model=GroupResponse)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = GroupManagementService.get_group_by_id(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group
