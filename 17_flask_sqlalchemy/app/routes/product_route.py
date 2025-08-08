from flask import Blueprint
from app.controllers.product_controller import list_products, add_product

product_bp = Blueprint("product", __name__)

product_bp.route("/", methods=["GET"])(list_products)
product_bp.route("/", methods=["POST"])(add_product)
