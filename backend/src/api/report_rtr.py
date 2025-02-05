from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select

from db.db_session import get_session
from models.report import Report1  #, ProductPublic
from typing import List

router = APIRouter()


@router.get("/1", response_model=List[Report1])
def get_data_for_report1(db_session: Session = Depends(get_session)):
    objs = db_session.exec(select(Report1)).all()
    if not objs:
        raise HTTPException(detail=f"There are no data for selected criteria", status_code=status.HTTP_404_NOT_FOUND)
    return objs

