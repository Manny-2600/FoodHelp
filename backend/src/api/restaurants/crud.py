from src import db
from src.api.restuarants.models import restaurant


def get_all_restuarants():
    return restaurant.query.all()


def get_restuarant_by_id(restuarant_id):
    return restaurant.query.filter_by(id=restuarant_id).first()


def get_restuarants_by_rating(cuisine):
    return restaurant.query.filter_by(cuisine=cuisine).first()


def add_restuarant(restuarantname, cuisine):
    restaurant = restaurant(restuarantname=restuarantname, cuisine=cuisine)
    db.session.add(restaurant)
    db.session.commit()
    return restaurant


def update_restuarant(restaurant, restuarantname, cuisine):
    restaurant.restuarantname = restuarantname
    restaurant.cuisine = cuisine
    db.session.commit()
    return restaurant
