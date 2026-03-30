from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for

web_bp = Blueprint("web", __name__)

@web_bp.route("/")
def home():
    return redirect(url_for("web.login_page"))

@web_bp.route("/login")
def login_page():
    return render_template("login.html")
