"""
    main.py

    Viginere cipher
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""

def get_alpha_num(c : str) -> int:
    if (len(c) != 1):
        # print("Error: get_alpha_num() argument length not equal to 1")
        return -1
    elif (not c.isalpha()):
        # print("Error: get_alpha_num() argument non-alpha character")
        return -1
    num = ord(c.lower())
    num -= 97 # Lowercase alphabet begins at 97 in ascii table
    return num

def viginere(key : str, ciphertext : str) -> str:
    key_idx = 0
    key_length = len(key)
    plaintext = ""
    for c in ciphertext:
        c_num = get_alpha_num(c)
        if (c_num == -1):
            plaintext += c
            continue
        key_num = get_alpha_num(key[key_idx])
        plain_num = c_num - key_num
        if (plain_num < 0):
            plain_num += 26
        plaintext += chr(plain_num + 97)
        key_idx = (key_idx + 1) % key_length
    return plaintext

def main() -> None:
    # key = input("Enter key: ")
    key = "unheard"
    # ciphertext = input("Enter ciphertext: ")
    ciphertext = "wvyglv. oiphxifq: sbb onfz qulve. rgx: ssemddvyl"
    print("Ciphertext:")
    print(ciphertext)
    print("Decoded:")
    print(viginere(key, ciphertext))

if __name__ == "__main__":
    main()
