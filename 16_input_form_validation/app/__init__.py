import os
from flask import Flask
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from app.routes.contact_route import contact_bp

def create_app():
  load_dotenv()
  app = Flask(__name__)
  app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

  CSRFProtect(app)
  app.register_blueprint(contact_bp)
  return app
