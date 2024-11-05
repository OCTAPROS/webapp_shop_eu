from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate
from db.models.product import Product


def create_new_product(product: ProductCreate, db: Session, author_id: int = 1):
    product = Product(        
        title=product.title,
        slug=product.slug,
        content=product.content,
        author_id=author_id
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

def update_product_by_id(id:int, product: ProductUpdate, db: Session, author_id: int):
    product_in_db = db.query(Product).filter(Product.id==id).first()
    if not product_in_db:
        return {"error": f"product with id {id} does not exists"}
    # product_in_db.title = product.title
    # product_in_db.slug = product.slug
    # product_in_db.content = product.content
    db.add(product_in_db)
    db.commit()
    return product_in_db

def delete_product_by_id(id: int, db: Session, author_id: int):
    product_in_db = db.query(Product).filter(Product.id==id)
    if not product_in_db.first():
        return {"error": f"product with id {id} has not been found"}
    
    product_in_db.delete()
    db.commit()
    return {"msg": f"product with id {id} has been deleted!"}