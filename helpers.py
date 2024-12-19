 
import hashlib


def encode_password(password):
       return hashlib.md5(password.encode()).hexdigest()
        

def check_password(password_bd, input_password):
    if password_bd == encode_password(input_password):
        return True
    return False