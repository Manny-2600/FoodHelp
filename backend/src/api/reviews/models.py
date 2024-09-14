import os

from sqlalchemy.sql import func

from src import db


class Reviews(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id"), nullable=False
    )
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, restaurant_id, rating):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.rating = rating


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.reviews.admin import ReviewsAdminView

    admin.add_view(ReviewsAdminView(Review, db.session))
