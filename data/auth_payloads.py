VALID_AUTH_PAYLOAD = {
    "username": "admin",
    "password": "password123"
}

INVALID_USERNAME_PAYLOAD = {
    "username": "wrong_user",
    "password": "password123"
}

INVALID_PASSWORD_PAYLOAD = {
    "username": "admin",
    "password": "wrong_password"
}

MISSING_USERNAME_PAYLOAD = {
    "password": "password123"
}

MISSING_PASSWORD_PAYLOAD = {
    "username": "admin"
}

EMPTY_AUTH_PAYLOAD = {}

SQL_INJECTION_AUTH_PAYLOAD = {
    "username": "' OR '1'='1",
    "password": "' OR '1'='1"
}

LONG_USERNAME_PAYLOAD = {
    "username": "a" * 500,
    "password": "password123"
}

LONG_PASSWORD_PAYLOAD = {
    "username": "admin",
    "password": "a" * 500
}