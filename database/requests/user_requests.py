from database.base import session
from database.tables import User


def create_user_db(telegram_id: int):
    user = User(telegram_id=telegram_id)
    session.add(user)
    session.commit()
    return user.telegram_id
