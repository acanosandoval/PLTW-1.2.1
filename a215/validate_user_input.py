#   a215.validate_user_input.py
import a212.rsa as rsa

key = input("Enter the Encryption Key: " )
while not key.isdigit():
    print("Invalid key")
    key = input("Enter valid Encryption Key: " )
key = int(key)

mod_value = input("Enter the Modulus: " )
while not mod_value.isdigit():
    print("Invalid Modulus")
    mod_value = input("Enter valid Modulus: " )
mod_value = int(mod_value)

plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)