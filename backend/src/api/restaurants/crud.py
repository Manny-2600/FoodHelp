from src import db
from src.api.restuarants.models import restuarant


def get_all_restuarants():
    return restuarant.query.all()


def get_restuarant_by_id(restuarant_id):
    return restuarant.query.filter_by(id=restuarant_id).first()


def get_restuarant_by_cuisine(cuisine):
    return restuarant.query.filter_by(cuisine=cuisine).first()


def add_restuarant(restuarantname, cuisine):
    restuarant = restuarant(restuarantname=restuarantname, cuisine=cuisine)
    db.session.add(restuarant)
    db.session.commit()
    return restuarant


def update_restuarant(restuarant, restuarantname, cuisine):
    restuarant.restuarantname = restuarantname
    restuarant.cuisine = cuisine
    db.session.commit()
    return restuarant
