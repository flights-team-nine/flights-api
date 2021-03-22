from flask import Flask
from flask_restful import Api
from src.resources.busses import BusResource

app = Flask(__name__)
api = Api(app)

api.add_resource(BusResource, '/busses/<int:bus_id>')

if __name__ == '__main__':
    app.run(debug=False)
