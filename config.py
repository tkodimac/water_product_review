import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "62c_windmill_street")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "False")
os.environ.setdefault("DATABASE_URL", "postgresql:///app")


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '62c_windmill_street'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
                'DATABASE_URL'
        ) or 'postgresql://keviny:rebecca@localhost/water_product_review.db'
