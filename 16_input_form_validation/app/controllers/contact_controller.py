from flask import render_template, redirect, session, url_for
from app.models.contact_form import ContactForm

def show_contact_form():
  form = ContactForm()

  if "form_data" in session:
    form_data = session["form_data"]
    form.name.data = form_data.get("name", "")
    form.email.data = form_data.get("email", "")
    form.message.data = form_data.get("message", "")
    session.pop("form_data")

  return render_template("contact.html", form=form)

def submit_contact_form():
  form = ContactForm()
  
  contact_data = {
    "name": form.name.data,
    "email": form.email.data,
    "message": form.message.data
  }
  
  if form.validate_on_submit(): 
    return render_template("contact_result.html", data=contact_data)
  else:
    session["form_data"] = contact_data
  return redirect(url_for("contact.contact_get"))


