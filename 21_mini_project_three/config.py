import os
from dotenv import load_dotenv

# define absolute path to project directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Load environment variable from .env file
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Set Flask application configuration from .env file."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'instance', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
