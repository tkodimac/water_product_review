from app import create_app, db,os


app = create_app()

with app.app_context():
    db.create_all()  # This creates the tables if they do not exist

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("DEBUG", False))
    