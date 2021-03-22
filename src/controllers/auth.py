from src.utilities.database import SessionLocal
from src.models.auth import Auth
from src.models.user import User
from typing import List
import bcrypt


def login(username: str, password: str):
    auth = Auth(Auth.username == username)
    return bcrypt.verify(password, auth.password)


def create(user: User, username: str, password: str, roles: List[str]):
    """ TODO """
    user = Auth(username=username, password=password,
                user_id=user.id)  # gotta hash
    return True
