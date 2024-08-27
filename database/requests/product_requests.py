import random

from database.base import session
from database.tables import Product


def create_product_db(name: str, description: str, price: float, amount: int, image: str) -> int:
    product = Product(
        id=random.randint(0, 10 ** 9),
        name=name,
        description=description,
        price=price,
        amount=amount,
        image=image
    )
    session.add(product)
    session.commit()
    return product.id


def get_available_product_db():
    return session.query(Product).where(Product.amount > 0).all()
