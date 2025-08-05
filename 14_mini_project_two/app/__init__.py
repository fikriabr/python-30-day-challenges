from flask import Flask


def create_app():
  app = Flask(__name__)
  
  # Register the quote blueprint
  from app.routes.quote_route import quote 
  app.register_blueprint(quote)

  return app
