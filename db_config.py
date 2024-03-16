import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to configure the database path and URI
def configure_database(app):
    db_path = os.getenv('DATABASE_PATH')
    if not db_path:
        raise RuntimeError("DATABASE_PATH is not set")
    os.makedirs(db_path, exist_ok=True)

    project_dir = Path(__file__).resolve().parent
    db_uri = f'sqlite:///{project_dir}/{db_path}/store.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
