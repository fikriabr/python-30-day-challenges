from flask import Flask
from app.routes.user_route import user_routes

def create_app():
  app = Flask(__name__)
  app.register_blueprint(user_routes)
  return app
