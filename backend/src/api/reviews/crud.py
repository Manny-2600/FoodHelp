from src import db
from src.api.reviews.models import Review


def get_all_reviews():
    return Review.query.all()


def get_reviews_by_id(review_id):
    return Review.query.filter_by(id=review_id).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user, username, email):
    user.username = username
    user.email = email
    db.session.commit()
    return user


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    return user
