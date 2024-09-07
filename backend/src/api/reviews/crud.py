from src import db
from src.api.reviews.models import Review


def get_all_reviews():
    return Review.query.all()


def get_review_by_id(review_id):
    return Review.query.filter_by(id=review_id).first()


def get_reviews_by_restaurant(restaurant_id):
    return Review.query.filter_by(restaurant_id=restaurant_id).all()


def get_reviews_by_user(user_id):
    return Review.query.filter_by(user_id=user_id).all()


def get_reviews_composite(user_id, restaurant_id):
    return Review.query.filter_by(user_id=user_id, restaurant_id=restaurant_id).all()


def add_review(user_id, restaurant_id, rating):
    review = Review(user_id=user_id, restaurant_id=restaurant_id, rating=rating)
    db.session.add(review)
    db.session.commit()
    return review


def update_review(review, rating):
    review.rating = rating
    db.session.commit()
    return review


def delete_review(review):
    db.session.delete(review)
    db.session.commit()
    return review
