from database.base import session
from database.tables import User


def create_user_db(telegram_id: int) -> int:
    user = User(telegram_id=telegram_id)
    session.add(user)
    session.commit()
    return user.telegram_id


def user_exists_db(telegram_id: int):
    user = session.query(User).where(User.telegram_id == telegram_id).first()
    return user is not None
