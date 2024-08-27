from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    telegram_id: Mapped[int] = mapped_column(primary_key=True)


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    image: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]


class Purchase(Base):
    __tablename__ = "purchase"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.telegram_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    price: Mapped[float]
