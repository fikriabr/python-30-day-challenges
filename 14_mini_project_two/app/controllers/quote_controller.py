from flask import jsonify
from app.services.quote_service import get_random_quote

def get_quote():
  quote = get_random_quote()
  return jsonify({
    "id": quote.id,
    "text": quote.text,
    "author": quote.author
  })