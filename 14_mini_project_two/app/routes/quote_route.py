from flask import Blueprint
from app.controllers.quote_controller import get_quote

quote = Blueprint('quote', __name__)

@quote.route('/quote', methods=['GET'])
def quote_route():
  return get_quote()