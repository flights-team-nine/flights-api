from datetime import datetime

from src.controllers.bus_book import create_bus_book, delete_bus_book, get_bus_books, update_bus_book
from src.controllers.mission import get_active_mission
from sqlalchemy.orm.session import Session
from src.utilities.database import SessionLocal
from flask.globals import request
from src.controllers.auth import check_token
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=False)
parser.add_argument('name', type=str, required=False)
parser.add_argument('mission', type=int, required=False)
parser.add_argument('driver', type=int, required=False)
parser.add_argument('destination', type=str, required=False)
parser.add_argument('arrival', type=str, required=False)
parser.add_argument('departure', type=str, required=False)


class BusResource(Resource):
    def get(self):
        db: Session = SessionLocal()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        if "photographer" in user_roles:
            return {"message": "access denied"}, 403
        else:
            mission = get_active_mission(db)
            book = get_bus_books(db, mission.id)
            return book, 200

    def post(self):
        args = parser.parse_args()
        db: Session = Session()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        arrival = datetime.strptime(
            args['arrival'], '%Y-%m-%d %H:%M:%S.%f')
        departure = datetime.strptime(
            args['departure'], '%Y-%m-%d %H:%M:%S.%f')
        if "admin" in user_roles:
            book = create_bus_book(db, args['name'], args['mission'], args['driver'],
                                   args['destination'], arrival, departure)
            return book, 201
        else:
            return {"message": "access denied"}, 403

    def put(self):
        args = parser.parse_args()
        db: Session = Session()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        arrival = datetime.strptime(
            args['arrival'], '%Y-%m-%d %H:%M:%S.%f')
        departure = datetime.strptime(
            args['departure'], '%Y-%m-%d %H:%M:%S.%f')
        if "admin" in user_roles:
            book = update_bus_book(db, args['bus_id'], args['name'], args['mission'], args['driver'],
                                   args['destination'], arrival, departure)
            return book, 202
        else:
            return {"message": "access denied"}, 403

    def delete(self):
        args = parser.parse_args()
        db: Session = Session()
        stored_data = check_token(request.cookies.get('auth'))
        user_roles = stored_data['roles']
        if "admin" in user_roles:
            return delete_bus_book(db, args['id']), 200
        else:
            return {"message": "access denied"}, 403
