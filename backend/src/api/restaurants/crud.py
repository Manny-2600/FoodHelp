from src import db
<<<<<<< HEAD
from src.api.restuarants.models import restaurant
=======
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206

from src.api.reviews.models import Review
from src.api.restaurants.models import Restaurant
from sqlalchemy import func

<<<<<<< HEAD
def get_all_restuarants():
    return restaurant.query.all()
=======
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206

def get_all_restaurants():
    return Restaurant.query.all()

<<<<<<< HEAD
def get_restuarant_by_id(restuarant_id):
    return restaurant.query.filter_by(id=restuarant_id).first()
=======
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206

def get_restaurant_by_id(restuarant_id):
    return Restaurant.query.filter_by(id=restuarant_id).first()

<<<<<<< HEAD
def get_restuarants_by_rating(cuisine):
    return restaurant.query.filter_by(cuisine=cuisine).first()
=======
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206

def get_rating_by_id(restuarant_id):
    return (
        db.session.query(func.avg(Review.rating)).filter_by(id=restuarant_id).scalar()
    )

<<<<<<< HEAD
def add_restuarant(restuarantname, cuisine):
    restaurant = restaurant(restuarantname=restuarantname, cuisine=cuisine)
    db.session.add(restaurant)
=======

def get_restaurant_by_name(restaurant_name):
    # exact name search
    return Restaurant.query.filter_by(name=restaurant_name).first()


def add_restaurant(restuarantname, cuisine):
    restuarant = Restaurant(name=restuarantname, cuisine=cuisine)
    db.session.add(restuarant)
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206
    db.session.commit()
    return restaurant


<<<<<<< HEAD
def update_restuarant(restaurant, restuarantname, cuisine):
    restaurant.restuarantname = restuarantname
    restaurant.cuisine = cuisine
    db.session.commit()
    return restaurant
=======
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
>>>>>>> ce0d0923bf07704b5ca93e2bc4eaecc1e3b1e206
