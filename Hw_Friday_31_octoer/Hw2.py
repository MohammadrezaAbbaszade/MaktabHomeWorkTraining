def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False

    for ch in password:
    if ch.islower():
    has_lower = True
    elif ch.isupper():
    has_upper = True
    elif ch.isspace():
    return False

return has_upper and has_lower


print(validate_password("dsdAAAfds"))