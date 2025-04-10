import re

def is_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+]", password):
        return False
    return True

password = "@Alphatech12345"

if is_strong(password):
    print("Your Password is strong...")
else:
    print("Your Password is not strong!!")