from flask.globals import request
from src.controllers.auth import check_token
from sqlalchemy.orm.session import Session
from src.utilities.database import SessionLocal
from src.controllers.veterans import get_veteran
from flask_restful import Resource


class VeteranResource(Resource):
    def get(self, id: int):
        db: Session = SessionLocal()
        veteran = get_veteran(db, id)
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        if "photographer" in user_roles:
            return {"message": "access denied"}, 403
        else:
            return veteran, 200
