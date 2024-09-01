from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, TextAreaField, IntegerField
)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError
)
from app.models import User

class RegistrationForm(FlaskForm):
    """Form for user registration."""
    username = StringField('Username', validators=[DataRequired(), 
                                                    Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                        validators=[DataRequired(), 
                                                    EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validate that the username is unique."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.'
                )

    def validate_email(self, email):
        """Validate that the email is unique."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.'
                )

class LoginForm(FlaskForm):
    """Form for user login."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ReviewForm(FlaskForm):
    """Form for submitting product reviews."""
    product_name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ml = IntegerField('Volume (ml)', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

    def __init__(self, *args, **kwargs):
        """Initialize form with optional review data for editing."""
        self.review_instance = kwargs.pop('review_instance', None)
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        if self.review_instance:
            # Prefill the form fields with existing review data
            self.product_name.data = self.review_instance.product_name
            self.description.data = self.review_instance.description
            self.ml.data = self.review_instance.ml
            self.review.data = self.review_instance.review
