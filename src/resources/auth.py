from flask_restful import Resource


class AuthResource(Resource):
    def post(self, username: str, password: str):
        """"""
