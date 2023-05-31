import random 
import string 

def password_generator(length = 12):
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_char) for _ in range(length))
    print (password)
    return password
password_generator(14)