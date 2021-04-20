from src.resources.veterans import VeteranResource
from src.models.veterans import Veteran
from src.resources.busses import BusResource
from src.resources.teams import TeamsResource
from flask import Flask
from flask_restful import Api
from src.utilities.database import Base, engine, SessionLocal
from src.resources.auth import AuthResource
from src.controllers.auth import init_admin

Base.metadata.create_all(bind=engine)
try:
    init_admin(SessionLocal())
except Exception:
    print("admin already exists")

app = Flask(__name__)
api = Api(app)

api.add_resource(AuthResource, "/auth")
api.add_resource(TeamsResource, "/teams/<id:int>")
api.add_resource(BusResource, "/bus")
api.add_resource(VeteranResource, "/veteran/<id:int>")


if __name__ == '__main__':
    app.run(debug=False)
