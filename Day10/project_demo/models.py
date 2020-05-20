# from flask_app import db

from exts import db


class User(db.Model):
    __tablename__ = 'project_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    age = db.Column(db.Integer)
