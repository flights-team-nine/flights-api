from os import environ
from src.models.auth import Auth
from sqlalchemy.orm import Session
import bcrypt
import jwt


def login(db: Session, username: str, password: str):
    user = db.query(Auth).filter(Auth.username == username).first()
    if bcrypt.checkpw(password, user.password):
        return jwt.encode({"id": user.user_id, "roles": dict(user.roles)}, environ.get("JWT_SECRET"), algorithm="HS256").decode("UTF-8")
    else:
        return False


def check_token(token: str):
    return jwt.decode(token, environ.get("JWT_SECRET"), algorithms=["HS256"])
