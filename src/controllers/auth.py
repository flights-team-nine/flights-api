from os import environ
from src.models.auth import Auth
from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime
import jwt


def login(db: Session, username: str, password: str):
    user = db.query(Auth).filter(Auth.username == username).first()
    if bcrypt.checkpw(password.encode("UTF-8"), user.password.encode("UTF-8")):
        return jwt.encode({"id": user.user_id, "roles": user.roles, "exp": int(datetime.utcnow().timestamp()) + 21600}, environ.get("JWT_SECRET"), algorithm="HS256")
    else:
        return False


def check_token(token: str):
    return jwt.decode(token, environ.get("JWT_SECRET"), algorithms=["HS256"])


def init_admin(db: Session):
    user = Auth(
        username=environ.get("ADMIN_USERNAME"), 
        password=bcrypt.hashpw(environ.get("ADMIN_PASSWORD").encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
        roles=["admin"]
    )
    db.add(user)
    db.commit()
    db.flush()