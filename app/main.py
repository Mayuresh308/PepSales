from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routers import customers  # 🔹 Import your customers router

# Load environment variables from .env file
load_dotenv()

# Get values from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

app = FastAPI()

# 🔹 Include the customers router
app.include_router(customers.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
