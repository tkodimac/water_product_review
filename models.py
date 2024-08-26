from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    reviews = db.relationship('WaterProductReview', backref='client', lazy=True)

class WaterProductReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
