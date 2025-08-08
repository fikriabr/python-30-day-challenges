from flask import request, jsonify
from app.services.product_service import get_all_products, create_product

def list_products():
  products = get_all_products()
  return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

def add_product():
  data = request.get_json()
  product = create_product(data["name"], data["price"])
  return jsonify({"id": product.id, "name": product.name, "price": product.price}), 201
