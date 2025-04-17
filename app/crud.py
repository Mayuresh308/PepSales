from sqlalchemy.orm import Session
from . import models, schemas

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100, min_price: float = 0, max_price: float = 10000, sort_by: str = 'name'):
    query = db.query(models.Product)
    
    if min_price:
        query = query.filter(models.Product.price >= min_price)
    if max_price:
        query = query.filter(models.Product.price <= max_price)
    
    if sort_by == 'price_asc':
        query = query.order_by(models.Product.price)
    elif sort_by == 'price_desc':
        query = query.order_by(models.Product.price.desc())
    else:
        query = query.order_by(models.Product.name)
    
    return query.offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(email=customer.email, name=customer.name, password_hash=customer.password)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(customer_id=order.customer_id, product_ids=','.join(map(str, order.product_ids)))
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
