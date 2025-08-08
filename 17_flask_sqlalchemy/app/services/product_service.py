from app import db
from app.models.product_model import Product

def get_all_products():
    return Product.query.all()

def create_product(name, price):
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return new_product
