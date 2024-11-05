from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate
from db.models.product import Product
from datetime import datetime, timezone
import json


def create_new_product(product: ProductCreate, db: Session, author_id: int = 1):
    product = Product(        
        name=product.name,
        image_uri=product.image_uri,
        description=product.description,
        price=product.price,
        created_at = datetime.now(timezone.utc),
        modified_at = None
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def retrieve_product(id: int, db: Session):
    product = db.query(Product).filter(Product.id==id).first()
    return product

def list_products(db: Session):
    products = db.query(Product).all()
    return products

def update_product_by_id(id:int, product: ProductUpdate, db: Session):
    product_in_db = db.query(Product).filter(Product.id==id).first()
    if not product_in_db:
        return {"error": f"Product with id {id} does not exists"}
    product_in_db.image_uri = product.image_uri
    product_in_db.description = product.description
    product_in_db.price = product.price
    product_in_db.modified_at = datetime.now(timezone.utc)
    db.add(product_in_db)
    db.commit()
    return product_in_db

def delete_product_by_id(id: int, db: Session):
    product_in_db = db.query(Product).filter(Product.id==id)
    if not product_in_db.first():
        return {"error": f"Product with id {id} has not been found"}
        
    product_in_db.delete()
    db.commit()
    return {"msg": f"Product with id {id} has been deleted!"}