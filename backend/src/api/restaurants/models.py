import os
from geoalchemy2 import Geography
from src import db


class Restaurant(db.Model):

<<<<<<< HEAD

class restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant= db.Column(db.String(128), nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)
    
   
    def __init__(self, restaurant, cuisine):
        self.restaurant= restaurant
        self.cuisine= cuisine
=======
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206

    def serialize(self):
        return {
            "name": self.name,
            "cuisine": self.cuisine,
        }


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.restaurants.admin import RestaurantsAdminView

    admin.add_view(RestaurantsAdminView(Restaurant, db.session))
