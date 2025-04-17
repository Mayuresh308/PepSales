from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    return crud.create_order(db=db, order=order)
