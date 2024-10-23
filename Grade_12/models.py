from flask_sqlalchemy import SQLAlchemy
from Grade_12 import db, login
from flask_login import UserMixin


@login.user_loader
def user_loader(id):
    return db.session.get(User, int(id))


#creating db tables 
class User(db.Model, UserMixin): 
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    results = db.relationship("Result", backref="user", lazy=True)

#creating results database 
class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)
    math = db.Column(db.Integer)
    english = db.Column(db.Integer)
    applied_computing = db.Column(db.Integer)
    algorithmics = db.Column(db.Integer)
    total_marks = db.Column(db.Integer, default=0)
    grade = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey("users.id"))

