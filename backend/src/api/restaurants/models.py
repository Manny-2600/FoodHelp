from os
from sqlalchemy.sql import func

from src import db




class restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant= db.Column(db.String(128), nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)
    
   
    def __init__(self, restaurant, cuisine):
        self.restaurant= restaurant
        self.cuisine= cuisine

