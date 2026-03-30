def validate_username_and_password(username, password):
    if not username:
        return "Username is required."

    if not password:
        return "Password is required."

    return None



def validate_amount(amount_text):
    if amount_text is None:
        return None, "Amount is required."

    cleaned_amount = str(amount_text).strip()
    if cleaned_amount == "":
        return None, "Amount is required."

    try:
        amount = float(cleaned_amount)
    except ValueError:
        return None, "Amount must be a number."

    if amount <= 0:
        return None, "Amount must be greater than zero."

    return amount, None
