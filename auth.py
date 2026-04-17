import bcrypt
import hmac
import secrets

USERS_DB = {
    "alice": {"password_hash": b"$2b$12$KIXpS/ZqCscE.t/1Q3xZnu6D.K7yY5vQ7QZfG1u5W7S5Q7QZfG1u5", "role": "admin"},
    "bob":   {"password_hash": b"$2b$12$L7pW9X7.8Q3xZnu6D.K7yY5vQ7QZfG1u5W7S5Q7QZfG1u5W7S5Q", "role": "user"},
}

SESSIONS = {}

def authenticate(username, password):
    user = USERS_DB.get(username)
    if user and bcrypt.checkpw(password.encode(), user["password_hash"]):
        return True
    return False

def is_admin(username):
    user = USERS_DB.get(username)
    if not user:
        return False
    return user["role"] == "admin"

def verify_api_key(provided_key, stored_key):
    return hmac.compare_digest(provided_key, stored_key)

def login(username, password):
    if not authenticate(username, password):
        return None
    token = secrets.token_hex(32)
    SESSIONS[token] = {"username": username}
    return token