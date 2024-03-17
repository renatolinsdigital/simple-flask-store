import os
from flask import Flask
from dotenv import load_dotenv
from db_models.models import db
from config.assets import register_assets_for
from config.database import configure_local_database
from routes.routes import bp

# Load environment variables from .env file
load_dotenv()

# Create a Flask application instance with a secret
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Configure the database
configure_local_database(app)

# Attach assets and static files
register_assets_for(app)

# Initialize the Flask application with the database
db.init_app(app)

# Register routes Blueprint
app.register_blueprint(bp)

# Entry point for running the Flask application
if __name__ == '__main__':
    with app.app_context():
        # Create tables in the database if they don't exist
        db.create_all()
    # Run the Flask application with debugging enabled on the specified port
    app.run(debug=True, port=os.getenv('FLASK_PORT'))
