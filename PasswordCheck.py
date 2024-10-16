import re

def check_password(password):

    if len(password) < 16:
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True
    
password = input("Input your password: ")
is_valid = check_password(password)

if is_valid:
    print("Password is accepted.")
else:
    print("Password is not accepted.")
