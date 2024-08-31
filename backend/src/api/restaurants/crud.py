from src import db
from src.api.restuarants.models import Restuarant


def get_all_restuarants():
    return Restuarant.query.all()


def get_restuarant_by_id(restuarant_id):
    return Restuarant.query.filter_by(id=restuarant_id).first()


def get_restuarants_by_rating(cuisine):
    return Restuarant.query.filter_by(cuisine=cuisine).first()


def add_restuarant(restuarantname, cuisine):
    restuarant = Restuarant(restuarantname=restuarantname, cuisine=cuisine)
    db.session.add(restuarant)
    db.session.commit()
    return restuarant


def update_restuarant(restuarant, restuarantname, cuisine):
    restuarant.restuarantname = restuarantname
    restuarant.cuisine = cuisine
    db.session.commit()
    return restuarant
