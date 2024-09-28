import os

# from geoalchemy2 import Geography
from src import db


class Restaurant(db.Model):

    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def serialize(self):
        return {
            "name": self.name,
            "cuisine": self.cuisine,
        }


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.restaurants.admin import RestaurantsAdminView

    admin.add_view(RestaurantsAdminView(Restaurant, db.session))
