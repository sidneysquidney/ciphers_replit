import random

import caesar_cipher, vinegar_cipher, substitution_cipher, cipher_functions

# decrypt an unknown text by a string
def cipher_master_unknown(text):
    if cipher_functions.is_vinegar(text):
        return vinegar_cipher.decrypt_unknown(text)
    elif cipher_functions.is_caesar(text):
        return caesar_cipher.decrypt_unknown(text)
    return substitution_cipher.decrypt_unknown(text)

# decrypt or encrypt a message helper function - encryption/decryption and the key
def decision(cipher_name):
    while True:
        method = input('(e)ncrypt or (d)ecrypt?')
        if method == 'e' or method == 'd':
            key = cipher_name.get_key()
            return method, key
        
# encrypt or decript
def eord():
    while True:
        m = input('(e)ncrypt or (d)ecrypt?')
        if m == 'e' or m == 'd':
            return m
        
# cipher known
def know_cipher():
    while True:
        k = input('do you know the cipher? y/n')
        if k == 'y':
            return True
        elif k == 'n':
            return False

# what type of cipher to use
def cipher_type():
    while True:
        cipher = input('Would you like to use the (c)aesar, (s)ubstitution, or (v)inegar cipher')
        if cipher == 'c':
            return caesar_cipher
        elif cipher == 's':
            return substitution_cipher
        elif cipher == 'v':
            return vinegar_cipher

# takes you through all cipher options by user input
def master_cipher():
    text = input('Enter a text:')
    method = eord()
    if method == 'e':
        cipher_name = cipher_type()
        key = cipher_name.get_key()
        print(cipher_name.encrypt(text, key))
    else:
        cipher_known = know_cipher()
        if cipher_known:
            cipher_name = cipher_type()
            key = cipher_name.get_key()
            if key == 'unknown':
                print(cipher_name)
                print(cipher_name.decrypt_unknown(text))
            else:
                print(cipher_name.decrypt(text, key))
        else:
            print(cipher_master_unknown(text))

if __name__ == '__main__':
    master_cipher()