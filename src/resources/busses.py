from flask_restful import Resource


class BusResource(Resource):
    def __init__(self):
        self.__id = 100

    def get(self, bus_id: int):
        return {"logged_in": bus_id == self.__id}
