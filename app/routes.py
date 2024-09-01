from flask import (
    render_template, url_for, flash, redirect, 
    Blueprint, request, abort
    )
from app.forms import RegistrationForm, LoginForm, ReviewForm
from app.models import User, WaterProductReview
from flask_login import login_user, current_user, logout_user, login_required
from app import bcrypt  # Import the initialized bcrypt instance
from app import db

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """Render the home page with all reviews."""
    reviews = WaterProductReview.query.all()
    return render_template('index.html', reviews=reviews)


@main.route("/register", methods=['GET', 'POST'])
def register():
    from app import db, bcrypt  # Import inside the function
    """Register a new user."""
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
        flash('Your account has been created! You can log in', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', title='Register', form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    """Log in an existing user."""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
           user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful.Check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@main.route("/logout")
def logout():
    """Log out the current user."""
    logout_user()
    return redirect(url_for('main.home'))


@main.route("/submit_review", methods=['GET', 'POST'])
@login_required
def submit_review():
    """Submit a product review."""
    form = ReviewForm()
    if form.validate_on_submit():
        review = WaterProductReview(
            product_name=form.product_name.data,
            description=form.description.data,
            ml=form.ml.data,
            review=form.review.data,
            author=current_user
        )
        db.session.add(review)
        try:
            db.session.commit()
            flash('Your review has been submitted!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred while submitting your review: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

    return render_template('submit_review.html', title='Submit Review', form=form, review=None)

@main.route("/review/<int:review_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_review(review_id):
    """Edit an existing review."""
    review = WaterProductReview.query.get_or_404(review_id)
    if review.author != current_user:
        abort(403)  # Forbidden: the user doesn't have the rights to edit this review

    form = ReviewForm()
    if form.validate_on_submit():
        review.product_name = form.product_name.data
        review.description = form.description.data
        review.ml = form.ml.data
        review.review = form.review.data
        try:
            db.session.commit()
            flash('Your review has been updated!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred while updating your review: {str(e)}', 'danger')
        return redirect(url_for('main.reviews'))
    elif request.method == 'GET':
        # Pre-fill the form with the existing review data
        form.product_name.data = review.product_name
        form.description.data = review.description
        form.ml.data = review.ml
        form.review.data = review.review

    return render_template('submit_review.html', title='Edit Review', form=form, review=review)

@main.route("/review/<int:review_id>/delete", methods=['POST'])
@login_required
def delete_review(review_id):
    """Delete an existing review."""
    review = WaterProductReview.query.get_or_404(review_id)
    if review.author != current_user:
        abort(403)  # Forbidden: the user doesn't have the rights to delete this review

    db.session.delete(review)
    try:
        db.session.commit()
        flash('Your review has been deleted!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred while deleting your review: {str(e)}', 'danger')

    return redirect(url_for('main.reviews'))


@main.route("/reviews")
@login_required
def reviews():
    """Display the current user's reviews."""
    reviews = WaterProductReview.query.filter_by(author=current_user).all()
    return render_template(
        'reviews.html', title='Your Reviews', reviews=reviews
    )

@main.route("/about")
def about():
    """Render the About Us page."""
    return render_template('about.html', title='About Us')
