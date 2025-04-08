# Task 11 
    #1.	Create custom_module.py:
secret = "shazam!"  # Initial value

def set_secret(new_secret):
    """Updates the secret variable globally."""
    global secret  
    secret = new_secret

     