import sys
import os
from models.db import SessionLocal
from models.user_models import User

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

users = [
    User(id=1, email="george.bluth@reqres.in", first_name="George", last_name="Bluth",
         avatar="https://reqres.in/img/faces/1-image.jpg"),
    User(id=2, email="janet.weaver@reqres.in", first_name="Janet", last_name="Weaver",
         avatar="https://reqres.in/img/faces/2-image.jpg"),
    User(id=3, email="emma.wong@reqres.in", first_name="Emma", last_name="Wong",
         avatar="https://reqres.in/img/faces/3-image.jpg"),
    User(id=4, email="eve.holt@reqres.in", first_name="Eve", last_name="Holt",
         avatar="https://reqres.in/img/faces/4-image.jpg"),
    User(id=5, email="charles.morris@reqres.in", first_name="Charles", last_name="Morris",
         avatar="https://reqres.in/img/faces/5-image.jpg"),
    User(id=6, email="tracey.ramos@reqres.in", first_name="Tracey", last_name="Ramos",
         avatar="https://reqres.in/img/faces/6-image.jpg"),
]


def seed():
    db = SessionLocal()
    for user in users:
        existing = db.query(User).filter_by(id=user.id).first()
        if not existing:
            db.add(user)
    db.commit()
    db.close()


if __name__ == "__main__":
    seed()
