import random


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_list = list(letters)
    key = {}
    for letter in letters:
        key[letter] = letters_list.pop(random.randint(0, len(letters_list) - 1))
    return key


def encrypt(key, message):
    cipher = ""
    for letter in message:
        if letter in key:
            cipher += key[letter]
        else:
            cipher += letter
    return cipher


def decrypt_key(key):
    decrypted_key = {}
    for k, v in key.items():
        decrypted_key[v] = k
    return decrypted_key


def decrypt(key, cipher):
    decrypted_key = decrypt_key(key)
    return encrypt(decrypted_key, cipher)