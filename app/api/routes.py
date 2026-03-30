from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import request

from app.services.account_service import deposit_money
from app.services.account_service import get_balance
from app.services.account_service import withdraw_money
from app.services.auth_service import authenticate_user
from app.services.transaction_service import get_transactions
from app.services.transaction_service import transfer_money


api_bp = Blueprint("api", __name__, url_prefix="/api")



def get_storage():
    return current_app.config["STORAGE"]


@api_bp.route("/login", methods=["POST"])
def api_login():
    data = request.get_json(silent=True) or {}

    username = str(data.get("username", "")).strip()
    password = str(data.get("password", ""))

    storage = get_storage()
    user, error_message = authenticate_user(storage, username, password)

    if error_message is not None:
        return jsonify({"success": False, "message": error_message}), 401

    return jsonify(
        {
            "success": True,
            "username": username,
            "full_name": user["full_name"],
            "account_id": user["account_id"],
        }
    ), 200


@api_bp.route("/accounts/<account_id>/balance", methods=["GET"])
def api_balance(account_id):
    storage = get_storage()
    username, user = storage.get_user_by_account_id(account_id)

    if user is None:
        return jsonify({"success": False, "message": "Account was not found."}), 404

    balance = get_balance(storage, username)
    return jsonify(
        {
            "success": True,
            "account_id": account_id,
            "username": username,
            "full_name": user["full_name"],
            "balance": balance,
        }
    ), 200


@api_bp.route("/accounts/<account_id>/deposit", methods=["POST"])
def api_deposit(account_id):
    data = request.get_json(silent=True) or {}
    amount_text = data.get("amount", "")

    storage = get_storage()
    username, user = storage.get_user_by_account_id(account_id)

    if user is None:
        return jsonify({"success": False, "message": "Account was not found."}), 404

    new_balance, error_message = deposit_money(storage, username, amount_text)
    if error_message is not None:
        return jsonify({"success": False, "message": error_message}), 400

    return jsonify(
        {
            "success": True,
            "account_id": account_id,
            "new_balance": new_balance,
        }
    ), 200


@api_bp.route("/accounts/<account_id>/withdraw", methods=["POST"])
def api_withdraw(account_id):
    data = request.get_json(silent=True) or {}
    amount_text = data.get("amount", "")

    storage = get_storage()
    username, user = storage.get_user_by_account_id(account_id)

    if user is None:
        return jsonify({"success": False, "message": "Account was not found."}), 404

    new_balance, error_message = withdraw_money(storage, username, amount_text)
    if error_message is not None:
        return jsonify({"success": False, "message": error_message}), 400

    return jsonify(
        {
            "success": True,
            "account_id": account_id,
            "new_balance": new_balance,
        }
    ), 200


