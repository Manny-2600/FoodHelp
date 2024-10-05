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


def add_restaurant(name, cuisine):
    restaurant = Restaurant(name=name, cuisine=cuisine)
    db.session.add(restaurant)
    db.session.commit()
    return restaurant


def update_restaurant(restaurant, name, cuisine):
    restaurant.name = name
    restaurant.cuisine = cuisine
    db.session.commit()
    return restaurant


def get_top_restaurants_by_cuisine(cuisine):
    # Query restaurants by cuisine
    restaurant_list = Restaurant.query.filter_by(cuisine=cuisine).all()

    # Sort the restaurant list by their average rating
    # We'll use the `get_rating_by_id` function to get the average rating of each restaurant
    # print("Restaurants: ", restaurant_list)
    # print(restaurant_list[0].id)
    # print(get_rating_by_id(restaurant_list[0].id))

    def get_rating_by_restaurant_id_is_available(rid):
        try:
            res = get_rating_by_id(rid)
        except:
            res = 0

        if not res:
            return 0
        return res

    sorted_restaurants = sorted(
        restaurant_list,
        key=lambda restaurant: get_rating_by_restaurant_id_is_available(restaurant.id),
        reverse=True,
    )

    return sorted_restaurants
