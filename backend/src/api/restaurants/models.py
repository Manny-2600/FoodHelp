from os
from sqlalchemy.sql import func

from src import db




class Restuarant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restuarant= db.Column(db.String(128), nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)
    
   
    def __init__(self, restuarant, cuisine):
        self.restuarant= restuarant
        self.cuisine = cuisine

