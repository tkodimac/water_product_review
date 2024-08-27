import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '62c_windmill_street'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://keviny:rebecca@localhost/water_product_review'
    

