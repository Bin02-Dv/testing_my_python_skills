import re

def is_valid_email(email):
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    return re.match(pattern, email) is not None


email = "myemail@gmail.com"

if is_valid_email(email):
    print(f"{email} is a valid email...")
    
else:
    print(f"{email}, is not a valid email!!")