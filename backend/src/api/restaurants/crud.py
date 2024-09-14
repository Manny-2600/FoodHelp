from src import db

from src.api.reviews.models import Review
from src.api.restaurants.models import Restaurant
from sqlalchemy import func


def get_all_restaurants():
    return Restaurant.query.all()


def get_restaurant_by_id(restuarant_id):
    return Restaurant.query.filter_by(id=restuarant_id).first()


def get_rating_by_id(restuarant_id):
    return (
        db.session.query(func.avg(Review.rating)).filter_by(id=restuarant_id).scalar()
    )


def get_restaurant_by_name(restaurant_name):
    # exact name search
    return Restaurant.query.filter_by(name=restaurant_name).first()


def add_restaurant(restuarantname, cuisine):
    restuarant = Restaurant(name=restuarantname, cuisine=cuisine)
    db.session.add(restuarant)
    db.session.commit()
    return restuarant


def update_restaurant(restuarant, restuarantname, cuisine):
    restuarant.name = restuarantname
    restuarant.cuisine = cuisine
    db.session.commit()
    return restuarant


def get_top_restaurants_by_cuisine(cuisine):
    # Query restaurants by cuisine
    restaurant_list = Restaurant.query.filter_by(cuisine=cuisine).all()

    # Sort the restaurant list by their average rating
    # We'll use the `get_rating_by_id` function to get the average rating of each restaurant
    sorted_restaurants = sorted(
        restaurant_list,
        key=lambda restaurant: get_rating_by_id(restaurant.id),
        reverse=True,
    )

    return sorted_restaurants
