from flask import render_template, url_for, flash, redirect, Blueprint
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, ReviewForm
from app.models import User, WaterProductReview
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    reviews = WaterProductReview.query.all()
    return render_template('index.html', reviews=reviews)

@main.route("/register", methods=['GET', 'POST'])
def register():
    """
    User register their details inorder to login so that
    it brongs great user experience
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode('utf-8')
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(
            'Your account has been created! You are now able to log in',
            'success'
        )
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/submit_review", methods=['GET', 'POST'])
@login_required
def submit_review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = WaterProductReview(product_name=form.product_name.data, description=form.description.data, ml=form.ml.data, review=form.review.data, author=current_user)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been submitted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('submit_review.html', title='Submit Review', form=form)

@main.route("/reviews")
@login_required
def reviews():
    reviews = WaterProductReview.query.filter_by(author=current_user).all()
    return render_template('reviews.html', title='Your Reviews', reviews=reviews)
