from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserUpdate
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(        
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active = True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def list_users(db: Session):
    users = db.query(User).all()
    return users

def update_user_by_id(id:int, user: UserUpdate, db: Session, author_id: int):
    user_in_db = db.query(User).filter(user.id==id).first()
    if not user_in_db:
        return {"error": f"user with id {id} does not exists"}
    # user_in_db.title = user.title
    # user_in_db.slug = user.slug
    # user_in_db.content = user.content
    db.add(user_in_db)
    db.commit()
    return user_in_db

def delete_user_by_id(id: int, db: Session, author_id: int):
    user_in_db = db.query(User).filter(User.id==id)
    if not user_in_db.first():
        return {"error": f"user with id {id} has not been found"}
    
    user_in_db.delete()
    db.commit()
    return {"msg": f"user with id {id} has been deleted!"}

def get_user_by_id(id:int, user: UserUpdate, db: Session, author_id: int):
    user_in_db = db.query(User).filter(user.id==id).first()
    if not user_in_db:
        return {"error": f"user with id {id} does not exists"}
    # user_in_db.title = user.title
    # user_in_db.slug = user.slug
    # user_in_db.content = user.content
    db.add(user_in_db)
    db.commit()
    return user_in_db