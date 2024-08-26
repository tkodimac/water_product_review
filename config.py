import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/water_products_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
