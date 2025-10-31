from re import match


def validate_password(password: str) -> bool:
return bool(match( r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)\S{8,}$', password))
