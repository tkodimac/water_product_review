from flask import Flask, render_template, request, redirect, url_for
from models import db, Client, WaterProductReview
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_review', methods=['POST'])
def add_review():
    name = request.form['name']
    description = request.form['description']
    volume = request.form['volume']
    review = request.form['review']
    user_id = request.form['user_id']  # Assuming user is logged in

    new_review = WaterProductReview(name=name, description=description, volume=volume, review=review, user_id=user_id)
    db.session.add(new_review)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
