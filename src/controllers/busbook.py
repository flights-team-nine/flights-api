# Import from models & json library
from src.models.bus_book import BusBook
from src.models.bus_book_user import BusBookUser
import json

# Create bus_book dictionary and return a json string
def bus_book():
    x = {"id": BusBook.id, "name": BusBook.name, "mission": BusBook.mission}
    return json.dumps(x)

# Create bus_book_user dictionary and return a json string
def bus_book_user():
    x = {"user_id": BusBookUser.user_id, "book_id": BusBookUser.book_id}
    return json.dumps(x)
# Combine both if needed
#def bus_book_joined():
#    x = {
#        "id": BusBook.id,
#        "name": BusBook.name,
#        "mission": BusBook.mission,
#        "user_id": BusBookUser.user_id,
#        "book_id": BusBookUser.book_id
#    }
#    return json.dumps(x)
