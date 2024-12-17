from fastapi import FastAPI
from app.models.user import Base
from app.config import engine
app = FastAPI()
Base.metadata.create_all(engine)
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в интернет-магазин!"}

