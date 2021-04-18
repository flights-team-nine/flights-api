from flask_restful import Resource, reqparse
from src.controllers.auth import login
from src.utilities.database import SessionLocal


parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)


class AuthResource(Resource):
    def post(self):
        db = SessionLocal()
        arguments = parser.parse_args(strict=True, http_error_code=400)
        token = login(db, arguments['username'], arguments['password'])
        headers = [('Set-Cookie', f'auth={token}; HttpOnly')]
        return {"message": None}, 200, headers
