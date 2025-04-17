from pydantic import BaseModel
from typing import List

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    email: str
    name: str

class CustomerCreate(CustomerBase):
    password: str

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_id: int
    product_ids: List[int]

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True
