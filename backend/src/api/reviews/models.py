import os

from sqlalchemy.sql import func

from src import db


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, rating):
        self.rating = rating
        


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.users.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
