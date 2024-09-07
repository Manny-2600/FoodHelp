from flask import request
from flask_restx import Namespace, Resource, fields

from src.api.restaurants.crud import (  # isort:skip
    get_all_restuarants
    get_restuarant_by_id
    get_restuarants_by_rating 
    add_restuarant
    update_restuarant

)

restuarants_namespace = Namespace("restaurants")


restuarant = restaurants_namespace.model(
    "Restaurant",
    {
        "id": fields.Integer(readOnly=True),
        "restaurant": fields.String(required=True),
        "cuisine": fields.String(required=True),
       
    },
)

restaurant_post = restaurants_namespace.inherit(
    "Restauarant post", restaurant, {"password": fields.String(required=True)}
)


class restaurantsList(Resource):
    @restaurants_namespace.marshal_with(restaurant, as_list=True)
    def get(self):
        """Returns all restaurants."""
        return get_all_restaurants(), 200

    @restaurants_namespace.expect(restaurant_post, validate=True)  # updated
    @restaurants_namespace.response(201, "<restaurant_cuisine> was added!")
    @restaurants_namespace.response(400, "Sorry. That cuisine already exists.")
    def post(self):
        """Creates a new restaurant."""
        post_data = request.get_json()
        restaurantname = post_data.get("restaurantname")
        cuisine = post_data.get("cuisine")
        response_object = {}

        restaurant = get_restaurant_by_cuisine(cuisine)
        if restaurant:
            response_object["message"] = "Sorry. That cuisine already exists."
            return response_object, 400

        add_restaurant(restaurantname, cuisine)
        response_object["message"] = f"{cuisine} was added!"
        return response_object, 201


class restaurants(Resource):
    @restaurants_namespace.marshal_with(restaurant)
    @restaurants_namespace.response(200, "Success")
    @restaurants_namespace.response(404, "restaurant <restaurant_id> does not exist")
    def get(self, restaurant_id):
        """Returns a single restaurant."""
        restaurant = get_restaurant_by_id(restaurant_id)
        if not restaurant:
            restaurants_namespace.abort(404, f"restaurant {restaurant_id} does not exist")
        return restaurant, 200

    @restaurants_namespace.expect(restaurant, validate=True)
    @restaurants_namespace.response(200, "<restaurant_id> was updated!")
    @restaurants_namespace.response(400, "Sorry. That cuisine already exists.")
    @restaurants_namespace.response(404, "restaurant <restaurant_id> does not exist")
    def put(self, restaurant_id):
        """Updates a restaurant."""
        post_data = request.get_json()
        restaurantname = post_data.get("restaurantname")
        cuisine = post_data.get("cuisine")
        response_object = {}

        restaurant = get_restaurant_by_id(restaurant_id)
        if not restaurant:
            restaurants_namespace.abort(404, f"restaurant {restaurant_id} does not exist")

        if get_restaurant_by_cuisine(cuisine):
            response_object["message"] = "Sorry. That cuisine already exists."
            return response_object, 400

        update_restaurant(restaurant, restaurantname, cuisine)

        response_object["message"] = f"{restaurant.id} was updated!"
        return response_object, 200

    @restaurants_namespace.response(200, "<restaurant_id> was removed!")
    @restaurants_namespace.response(404, "restaurant <restaurant_id> does not exist")
    def delete(self, restaurant_id):
        """ "Deletes a restaurant."""
        response_object = {}
        restaurant = get_restaurant_by_id(restaurant_id)

        if not restaurant:
            restaurants_namespace.abort(404, f"restaurant {restaurant_id} does not exist")

        delete_restaurant(restaurant)

        response_object["message"] = f"{restaurant.cuisine} was removed!"
        return response_object, 200


restaurants_namespace.add_resource(restaurantsList, "")
restaurants_namespace.add_resource(restaurants, "/<int:restaurant_id>")
