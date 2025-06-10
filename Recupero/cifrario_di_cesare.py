from string import ascii_lowercase, ascii_uppercase

def cifrario_di_cesare(mess, chiav):
    """
    cifra il messaggio utilizzando ul cifrario di cesare
    :param mess: il messaggio da cifrare
    :param chiav: la chiave di cifratura
    :return: il messaggio cifrato
    """
    cifrato = ""
    for char in mess:
        if char.isalpha():
            shift = chiav % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
                cifrato += chr((ord(char) - base + shift) % 26 + base)
        else:
            cifrato += char
    return cifrato

print(cifrario_di_cesare("Ciao Mondo!", 3)) 

'''
def caesar_cypher_encrypt(s, key):
    encrypted_s = ""
    for char in s:
        if 'a' <= char <= 'z':
            start = ord('a')
            encrypted_char_code = (ord(char) - start + key) % 26 + start
            encrypted_s += chr(encrypted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            encrypted_char_code = (ord(char) - start + key) % 26 + start
            encrypted_s += chr(encrypted_char_code)
        else:
            encrypted_s += char
    return encrypted_s

def caesar_cypher_decrypt(s, key):
    decrypted_s = ""
    for char in s:
        if 'a' <= char <= 'z':
            start = ord('a')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_s += chr(decrypted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_s += chr(decrypted_char_code)
        else:
            decrypted_s += char
    return decrypted_s'''