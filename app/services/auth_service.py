from app.validators import validate_username_and_password



def authenticate_user(storage, username, password):
    error_message = validate_username_and_password(username, password)
    if error_message is not None:
        return None, error_message

    user = storage.get_user(username)
    if user is None:
        return None, "Invalid username or password."

    if user["password"] != password:
        return None, "Invalid username or password."

    return user, None
