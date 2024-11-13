from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List


from schemas.user import UserCreate, UserShow
from db.session import get_db
from db.repository.user import create_new_user, User


# from schemas.order import BlogCreate, BlogShow, BlogUpdate
# from db.session import get_db
# from db.models.user import User
from apis.v1.route_auth import get_current_user
from db.repository.user import create_new_user, get_user_by_id, list_users, update_user_by_id, delete_user_by_id

# router = APIRouter()

router = APIRouter()

@router.post("/", response_model=UserShow, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.get("/{id}", response_model=UserShow)
def get_blog_by_id(id:int, db: Session = Depends(get_db)):
    user = get_user_by_id(id=id, db=db)
    if not user:
        raise HTTPException(detail=f"Blog with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return user

@router.get("/", response_model=List[UserShow])
def get_all_users(db: Session = Depends(get_db)):
    user = list_users(db=db)
    if not user:
        raise HTTPException(detail=f"No user to retrieve", status_code=status.HTTP_404_NOT_FOUND)
    return user

@router.put("/{id}", response_model=UserShow)
def update_blog(id:int, blog: UserShow, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = update_user_by_id(id=id, blog=blog, db=db, author_id=current_user.id)
    if isinstance(blog, dict):
        raise HTTPException(
            detail=blog.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return blog

@router.delete("/{id}")
def delete_blog(id:int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    message = delete_user_by_id(id=id, db=db, author_id=current_user.id)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return message.get("msg")
