from flask import Blueprint
from app.controllers.contact_controller import show_contact_form, submit_contact_form

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["GET"])
def contact_get():
    print("Displaying contact form")
    return show_contact_form()

@contact_bp.route("/contact", methods=["POST"])
def contact_post():
    print("Contact form submitted")
    return submit_contact_form()
