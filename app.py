import os
from db_models.models import db
from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from routes.routes import bp

# Load environment variables from .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Handling database Path
db_path = os.getenv('DATABASE_PATH')
if not db_path:
    raise RuntimeError("DATABASE_PATH is not set")
os.makedirs(db_path, exist_ok=True)

# Handling database URI
project_dir = Path(__file__).resolve().parent
db_uri = f'sqlite:///{project_dir}/{db_path}/store.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

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
