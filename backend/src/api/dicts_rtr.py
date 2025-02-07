from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select, distinct
from db.db_session import get_session
from models.dict import DictRow, DictRowPublic
from typing import List



router = APIRouter()

@router.get("/_all_names_", response_model=List[str])
def get_all_dictionary_names(db_session: Session = Depends(get_session)):
    objs = db_session.exec(select(distinct(DictRow.dict_name))).all()
    if not objs:
        raise HTTPException(detail=f"There are no products for selected criteria", status_code=status.HTTP_404_NOT_FOUND)
    return objs


@router.get("/{dict_name}", response_model=list[DictRowPublic])
def get_dict_values_by_dict_name(dict_name:str, db_session: Session = Depends(get_session)):
    objs = db_session.exec(select(DictRow).where(DictRow.dict_name == dict_name.upper())).all()
    if not objs:
        raise HTTPException(detail=f"Dictionaly values for dict with name: {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return objs
