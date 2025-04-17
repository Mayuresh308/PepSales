from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers/", response_model=schemas.Customer)
def create(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.get("/customers/", response_model=list[schemas.Customer])
def read(db: Session = Depends(get_db)):
    return crud.get_customers(db)