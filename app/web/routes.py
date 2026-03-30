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

@web_bp.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@web_bp.route("/deposit")
def deposit_page():
    return render_template("deposit.html")

@web_bp.route("/withdraw")
def withdraw_page():
    return render_template("withdraw.html")
