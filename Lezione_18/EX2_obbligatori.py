def validet_passaword(password):
    if len (password) < 20:
        raise ValueError("passaword must be at least 20 characters long")
    uppercase_count = sum (1 for char in password if char.isupper())
    if uppercase_count < 3:
        raise ValueError("password must contain at least three uppercase letters. ")
    special_count = sum(1 for char in password if not char.isalnum())
    if special_count < 4:
        raise ValueError("Password must contain at least four special characters")
    return True
passaword_corretta = "AbCdEfGkkjerò8755'0837%&/%$£!!!=)?^"

try:
    print(validet_passaword(passaword_corretta))

except ValueError as e:
    print(e)
