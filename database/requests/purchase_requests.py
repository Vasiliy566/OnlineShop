import random

from database.base import session
from database.tables import Purchase, Product


def create_purchase_db(user_id: int, product_id: int, price: float) -> int:
    session.query(Product).where(Product.id == product_id).update({"amount": Product.amount - 1})
    session.commit()

    purchase = Purchase(id=random.randint(1, 10**9), user_id=user_id, product_id=product_id, price=price)
    session.add(purchase)
    session.commit()
    return purchase.id
