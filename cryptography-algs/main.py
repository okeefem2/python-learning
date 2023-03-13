
# Press the green button in the gutter to run the script.
from caesar_cipher import decrypt
from frequency_analysis import build_cipher_frequency, calculate_matches, guess_key, decrypt_guess

if __name__ == '__main__':

    cipher_letter_freq = build_cipher_frequency()
    letter_matches = calculate_matches(cipher_letter_freq)

    for k, v in letter_matches.items():
        print(k, v)
    key_guess = guess_key(letter_matches)
    print()
    print(key_guess)
    print(decrypt_guess(key_guess))




