from flask import Blueprint
from app.controllers.main_controller import index_page, about_page

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
  return index_page()

@main_bp.route('/about')
def about():
  return about_page()