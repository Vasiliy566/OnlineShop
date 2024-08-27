import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from database.requests.product_requests import create_product_db, get_available_product_db
from database.requests.user_requests import create_user_db

app = FastAPI()


class Product(BaseModel):
    name: str
    description: str
    price: float
    amount: int
    image: str = ""


@app.post("/products/")
def create_product(product: Product) -> int:
    return create_product_db(product.name, product.description, product.price, product.amount, product.image)


@app.post("/users/")
def create_user(user_id: int) -> int:
    return create_user_db(user_id)


@app.get("/products/")
def get_products():
    return get_available_product_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
