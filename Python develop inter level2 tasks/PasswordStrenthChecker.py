import re

def password_strength(password):
  
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
   
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password should contain at least one special character."
    
    
    return "Strong: Password meets all criteria."


password = input("Enter your password: ")


print(password_strength(password))
