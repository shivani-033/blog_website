from flask_sqlalchemy import SQLAlchemy 
from .import db , create_app
from datetime import datetime

class BlogUser(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(30) , nullable = False)
    password = db.Column(db.String(20) , nullable = False)

class BlogPost(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(50) , nullable = False)
    content = db.Column(db.String(50) , nullable = False)
    
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, default=True)