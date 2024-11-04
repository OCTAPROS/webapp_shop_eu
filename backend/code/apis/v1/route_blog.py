from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.blog import BlogCreate, BlogShow, BlogUpdate
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from db.repository.blog import create_new_blog, retrieve_blog, list_blogs, update_blog_by_id, delete_blog_by_id
from typing import List

router = APIRouter()

@router.post("/", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def create_blog(blog:BlogCreate, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db)
    return blog

@router.get("/{id}", response_model=BlogShow)
def get_blog_by_id(id:int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return blog

@router.get("/", response_model=List[BlogShow])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    if not blogs:
        raise HTTPException(detail=f"No blogs to retrieve", status_code=status.HTTP_404_NOT_FOUND)
    return blogs

@router.put("/{id}", response_model=BlogShow)
def update_blog(id:int, blog: BlogUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = update_blog_by_id(id=id, blog=blog, db=db, author_id=current_user.id)
    if isinstance(blog, dict):
        raise HTTPException(
            detail=blog.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return blog

@router.delete("/{id}")
def delete_blog(id:int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    message = delete_blog_by_id(id=id, db=db, author_id=current_user.id)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return message.get("msg")
