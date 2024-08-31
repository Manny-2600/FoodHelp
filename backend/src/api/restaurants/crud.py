from src import db
from src.api.restuarants.models import restuarant


def get_all_restuarants():
    return restuarant.query.all()


def get_restuarant_by_id(restuarant_id):
    return restuarant.query.filter_by(id=restuarant_id).first()


# get avg review rating by id (restaurant id)

# get restaurant by name


# get restaurant by cuisine sorted by rating


def add_restuarant(restuarantname, email):
    restuarant = restuarant(restuarantname=restuarantname, email=email)
    db.session.add(restuarant)
    db.session.commit()
    return restuarant


def update_restuarant(restuarant, restuarantname, email):
    restuarant.restuarantname = restuarantname
    restuarant.email = email
    db.session.commit()
    return restuarant


def delete_restuarant(restuarant):
    db.session.delete(restuarant)
    db.session.commit()
    return restuarant
