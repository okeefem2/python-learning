def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    index = n

    for letter in letters:
        rotated_index = index % len(letters)
        key[letter] = letters[rotated_index]
        index += 1
    return key


def encrypt(key, message):
    cipher = ""
    for letter in message:
        if letter in key:
            cipher += key[letter]
        else:
            cipher += letter
    return cipher


def reverse_key_map(key: dict):
    reverse_key = {}
    for k, v in key.items():
        reverse_key[v] = k
    return reverse_key


def decrypt_reverse_key(key: dict, cipher: str):
    reverse_key = reverse_key_map(key)
    return encrypt(reverse_key, cipher)


def decrypt(key, cipher):
    message = ""
    # could also just loop over the key and create a reverse mapping dict
    originals = list(key.keys())
    mapping = list(key.values())
    for letter in cipher:
        if letter in mapping:
            message += originals[mapping.index(letter)]
        else:
            message += letter
    return message


def calculate_rotation_value(key):
    a_ascii = ord('A')
    a_mapping = key['A']
    a_mapping_ascii = ord(a_mapping)
    return (a_mapping_ascii - a_ascii) % 26


def decrypt_reverse_key_rotation(key, cipher):
    rotation_value = calculate_rotation_value(key)
    reverse_key = generate_key(26 - rotation_value)
    return encrypt(reverse_key, cipher)


