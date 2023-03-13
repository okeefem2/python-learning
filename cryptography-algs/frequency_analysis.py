import operator

from substitution_cipher import decrypt

cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""


# Frequency distribution of letters in english
letter_freq = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()


def build_cipher_frequency():
    cipher_letter_freq = {}
    for c in alphabet:
        cipher_letter_freq[c] = 0

    total_letters = 0
    for c in cipher:
        if c in cipher_letter_freq:
            total_letters += 1
            cipher_letter_freq[c] += 1

    for k, v in cipher_letter_freq.items():
        cipher_letter_freq[k] = round(v / total_letters, 4)
    return cipher_letter_freq


def print_frequency(cipher_letter_freq):
    new_line_count = 0
    for c in cipher_letter_freq:
        print(c, ':', cipher_letter_freq[c], ' ', end='')
        if new_line_count % 3 == 2:
            print()
        new_line_count += 1


def calculate_matches(cipher_letter_freq):
    letter_mappings = {}
    for cipher_letter in alphabet:
        guess_map = {}
        for letter in alphabet:
            guess_map[letter] = round(abs(cipher_letter_freq[cipher_letter] - letter_freq[letter]), 4)
        letter_mappings[cipher_letter] = sorted(guess_map.items(), key=operator.itemgetter(1))
    return letter_mappings


def guess_key(letter_mappings):
    letters = list(alphabet)
    cipher_letters = list(alphabet)
    key = {}

    for cipher_letter in cipher_letters:
        # For each letter, get the mapping for the letter
        # By default this will be the one with lowest diff value
        # Once a letter has been used, remove it from the possible list so it isn't reused
        if cipher_letter not in letter_mappings:
            continue
        for letter, diff in letter_mappings[cipher_letter]:
            if letter in letters:
                key[cipher_letter] = letter
                # Remove the mapped letter from the  available letters
                letters.remove(letter)
                break
    return key


def decrypt_guess(key):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message

