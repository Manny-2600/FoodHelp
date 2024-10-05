from flask import request
from flask_restx import Namespace, Resource, fields, reqparse


from src.api.restaurants.crud import (  # isort:skip
    get_all_restaurants,
    get_restaurant_by_id,
    get_restaurant_by_name,
    add_restaurant,
    update_restaurant,
    get_rating_by_id,
    get_top_restaurants_by_cuisine,
)


restaurants_namespace = Namespace("restaurants")


restaurant = restaurants_namespace.model(
    "Restaurant",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "cuisine": fields.String(required=True),
    },
)


class RestaurantsList(Resource):
    @restaurants_namespace.marshal_with(restaurant, as_list=True)
    def get(self):
        """Returns all restaurants."""
        return get_all_restaurants(), 200

    @restaurants_namespace.expect(restaurant, validate=True)  # updated
    @restaurants_namespace.response(201, "<restaurant_name> was added!")
    @restaurants_namespace.response(400, "Sorry. That restaurant already exists.")
    def post(self):
        """Creates a new restaurant."""
        post_data = request.get_json()
        restaurantname = post_data.get("name")
        cuisine = post_data.get("cuisine")
        response_object = {}

        restaurant = get_restaurant_by_name(restaurantname)
        if restaurant:
            response_object["message"] = "Sorry. That cuisine already exists."
            return response_object, 400

        add_restaurant(restaurantname, cuisine)
        response_object["message"] = f"{cuisine} was added!"
        return response_object, 201


class Restaurants(Resource):
    @restaurants_namespace.marshal_with(restaurant)
    @restaurants_namespace.response(200, "Success")
    @restaurants_namespace.response(404, "Restaurant <restaurant_name> does not exist")
    def get(self, restaurant_id):
        """Returns a single restaurant."""
        restaurant = get_restaurant_by_id(restaurant_id)
        if not restaurant:
            restaurants_namespace.abort(
                404, f"restaurant {restaurant_id} does not exist"
            )
        return restaurant, 200

    @restaurants_namespace.expect(restaurant, validate=True)
    @restaurants_namespace.response(200, "<restaurant_id> was updated!")
    @restaurants_namespace.response(400, "Sorry. That restaurant already exists.")
    @restaurants_namespace.response(404, "Restaurant <restaurant_id> does not exist")
    def put(self, restaurant_id):
        """Updates a restaurant."""
        post_data = request.get_json()
        restaurantname = post_data.get("name")
        cuisine = post_data.get("cuisine")
        response_object = {}

        restaurant = get_restaurant_by_id(restaurant_id)
        if not restaurant:
            restaurants_namespace.abort(
                404, f"restaurant {restaurant_id} does not exist"
            )

        if get_restaurant_by_name(restaurantname):
            response_object["message"] = "Sorry. That restaurant already exists."
            return response_object, 400

        update_restaurant(restaurant, restaurantname, cuisine)

        response_object["message"] = f"{restaurant.id} was updated!"
        return response_object, 200


class RestaurantsSearches(Resource):
    @restaurants_namespace.marshal_with(restaurant, as_list=True)
    def get(self, restaurant_cuisine):
        """Return nearby restaurants of specific type."""

        # parser = reqparse.RequestParser()
        # parser.add_argument("cuisine", type=str, required=False)

        # args = parser.parse_args()
        # cuisine = args.get("restaurant_cuisine", "")

        # print("Searching by ", restaurant_cuisine)
        cuisine = restaurant_cuisine.replace("+", " ")
        print("Searching by ", cuisine)
        res = get_top_restaurants_by_cuisine(cuisine)

        return res, 200


class RestaurantRating(Resource):
    def get(self, restaurant_id):
        """Returns average rating for given restaurant id. 0 if there are no ratings."""
        response_object = {}
        restaurant = get_restaurant_by_id(restaurant_id)

        if not restaurant:
            restaurants_namespace.abort(
                404, f"Restaurant {restaurant_id} does not exist"
            )
        rating = get_rating_by_id(restaurant_id)
        return {"rating": int(rating)}, 200


restaurants_namespace.add_resource(RestaurantsList, "")
restaurants_namespace.add_resource(Restaurants, "/<int:restaurant_id>")
restaurants_namespace.add_resource(RestaurantsSearches, "/<string:restaurant_cuisine>")
restaurants_namespace.add_resource(RestaurantRating, "/rating/<int:restaurant_id>")
