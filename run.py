import os
from app import create_app, db


app = create_app()

with app.app_context():
    db.create_all()  # This creates the tables if they do not exist

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

#    port = int(os.environ.get("PORT", 5000))
#    app.run(host="0.0.0.0", port=port, debug=os.environ.get("DEBUG", False))