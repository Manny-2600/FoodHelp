from src import db
from src.api.restuarants.models import restuarant


def get_all_restuarants():
    return restuarant.query.all()


def get_restuarant_by_id(restuarant_id):
    return restuarant.query.filter_by(id=restuarant_id).first()


def get_restuarant_by_email(email):
    return restuarant.query.filter_by(email=email).first()


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
