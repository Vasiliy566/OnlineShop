import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database.requests.product_requests import create_product_db, get_available_product_db
from database.requests.purchase_requests import create_purchase_db
from database.requests.user_requests import create_user_db

app = FastAPI()
SECRET_KEY = "1234"


class Product(BaseModel):
    name: str
    description: str
    price: float
    amount: int
    image: str = ""


class Purchase(BaseModel):
    user_id: int
    product_id: int
    price: float


@app.post("/products/")
def create_product(product: Product, api_key: str) -> int:
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=403)
    return create_product_db(product.name, product.description, product.price, product.amount, product.image)


@app.post("/users/")
def create_user(user_id: int, api_key: str) -> int:
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=403)
    return create_user_db(user_id)


@app.post("/purchase/")
def create_purchase(purchase: Purchase, api_key: str) -> int:
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=403)
    return create_purchase_db(purchase.user_id, purchase.product_id, purchase.price)


@app.get("/products/")
def get_products(api_key: str):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=403)
    return get_available_product_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
