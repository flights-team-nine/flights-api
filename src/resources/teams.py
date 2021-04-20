from src.models.teams import Team
from src.controllers.teams import delete_team, get_teams, update_team
from src.controllers.auth import check_token
from flask.globals import request
from sqlalchemy.orm.session import Session
from src.utilities.database import SessionLocal
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=False)
parser.add_argument('name', type=str, required=False)
parser.add_argument('color', type=int, required=False)
parser.add_argument('leader', type=int, required=False)


class TeamsResource(Resource):
    def get(self, id: int):
        db: Session = SessionLocal()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        if "photographer" in user_roles:
            return {"message": "access denied"}, 403
        else:
            teams = get_teams(db, id)
            return teams, 200

    def post(self, id: int):
        db: Session = SessionLocal()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']

    def put(self, id: int):
        args = parser.parse_args()
        db: Session = SessionLocal()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        if "admin" in user_roles:
            team = update_team(db, args['id'], args['name'], args['color'], id)
            return team, 202
        else:
            return {"message": "access denied"}, 403

    def delete(self, id: int):
        db: Session = SessionLocal()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        if "admin" in user_roles:
            team = delete_team(db, id)
            return team, 202
        else:
            return {"message": "access denied"}, 403
