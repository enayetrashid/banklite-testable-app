from app.validators import validate_amount



def get_balance(storage, username):
    user = storage.get_user(username)
    if user is None:
        return None
    return user["balance"]



def deposit_money(storage, username, amount_text):
    amount, error_message = validate_amount(amount_text)
    if error_message is not None:
        return None, error_message

    current_balance = get_balance(storage, username)
    if current_balance is None:
        return None, "User was not found."

    new_balance = current_balance + amount
    storage.update_balance(username, new_balance)

    storage.add_transaction(
        username,
        {
            "type": "deposit",
            "amount": amount,
            "message": f"Deposited {amount:.2f}",
        },
    )

    return new_balance, None



def withdraw_money(storage, username, amount_text):
    amount, error_message = validate_amount(amount_text)
    if error_message is not None:
        return None, error_message

    current_balance = get_balance(storage, username)
    if current_balance is None:
        return None, "User was not found."

    if amount > current_balance:
        return None, "Insufficient funds."

    new_balance = current_balance - amount
    storage.update_balance(username, new_balance)

    storage.add_transaction(
        username,
        {
            "type": "withdraw",
            "amount": amount,
            "message": f"Withdrew {amount:.2f}",
        },
    )

    return new_balance, None
