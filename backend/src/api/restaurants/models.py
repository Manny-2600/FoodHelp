from os
from sqlalchemy.sql import func

from src import db




class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restuarant_name = db.Column(db.String(128), nullable=False)
    cuisine = db.Column(db.String(128), nullable=False)
    
   
    def __init__(self, restuarant_name, cuisine):
        self.restuarant_name = restuarant_name
        self.cuisine = cuisine

