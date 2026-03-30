from app.services.account_service import get_balance
from app.validators import validate_amount



def get_transactions(storage, username):
    return storage.list_transactions(username)



def transfer_money(storage, from_username, to_account_id, amount_text):
    amount, error_message = validate_amount(amount_text)
    if error_message is not None:
        return None, error_message

    to_username, target_user = storage.get_user_by_account_id(to_account_id)
    if target_user is None:
        return None, "Target account was not found."

    if to_username == from_username:
        return None, "You cannot transfer to your own account."

    sender_balance = get_balance(storage, from_username)
    if sender_balance is None:
        return None, "User was not found."

    if amount > sender_balance:
        return None, "Insufficient funds."

    receiver_balance = target_user["balance"]
    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount

    storage.update_balance(from_username, new_sender_balance)
    storage.update_balance(to_username, new_receiver_balance)

    storage.add_transaction(
        from_username,
        {
            "type": "transfer_out",
            "amount": amount,
            "message": f"Transferred {amount:.2f} to {to_account_id}",
        },
    )
    storage.add_transaction(
        to_username,
        {
            "type": "transfer_in",
            "amount": amount,
            "message": f"Received {amount:.2f} from {from_username}",
        },
    )

    return new_sender_balance, None
