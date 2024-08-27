# Water Product Review Platform

## Overview
This project is a web application that allows users to register, log in, and submit reviews for water products. The application is built using Flask (Python), with PostgreSQL as the database. The frontend uses HTML, CSS, and JavaScript.

## Features
- User Registration and Login
- CRUD Operations for Product Reviews
- User Authentication
- Responsive Navigation
- Deployed on Heroku

## Technologies
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Version Control**: Git & GitHub
- **Deployment**: Heroku

## Setup Instructions
1. Clone the repository: `git clone https://github.com/your-username/water-product-review.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment:
    - On macOS/Linux: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Set up the database:
    - Create a PostgreSQL database.
    - Update the `SQLALCHEMY_DATABASE_URI` in `config.py` with your database credentials.
6. Run the application: `python run.py`

## Deployment
The project is deployed on Heroku. Make sure to configure the environment variables on Heroku for `SECRET_KEY` and `DATABASE_URL`.

## License
This project is licensed under the MIT License.
