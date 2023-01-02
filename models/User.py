from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import app
from datetime import datetime

class User(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    username = app.db.Column(app.db.String, unique=True, nullable=False)
    email = app.db.Column(app.db.String)
    date_created = app.db.Column(app.db.DateTime, default = datetime.utcnow)
