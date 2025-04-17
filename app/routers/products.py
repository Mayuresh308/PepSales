from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models, database

router = APIRouter()

@router.get("/", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 100, min_price: float = 0, max_price: float = 10000, sort_by: str = 'name', db: Session = Depends(database.get_db)):
    return crud.get_products(db, skip, limit, min_price, max_price, sort_by)
