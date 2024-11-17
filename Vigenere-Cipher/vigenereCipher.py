# Vigenere Cipher

def encrypt(plaintext, key):
    key = padding(plaintext, key)
    result = ''
    for i in range(0, len(plaintext)):
        if ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90:
            charPt = ord(plaintext[i]) - 65
            if ord(key[i]) >= 65 and ord(key[i]) <= 90:
                charKey = ord(key[i]) - 65
            elif ord(key[i]) >= 97 and ord(key[i]) <= 122:
                charKey = ord(key[i]) - 97
            result += chr(((charPt + charKey) % 26) + 65)
        elif ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122:
            charPt = ord(plaintext[i]) - 97
            if ord(key[i]) >= 65 and ord(key[i]) <= 90:
                charKey = ord(key[i]) - 65
            elif ord(key[i]) >= 97 and ord(key[i]) <= 122:
                charKey = ord(key[i]) - 97
            result += chr(((charPt + charKey) % 26) + 97)
    return result

def decrypt(ciphertext, key):
    key = padding(ciphertext, key)
    result = ''
    for i in range(0, len(ciphertext)):
        if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
            charPt = ord(ciphertext[i]) - 65
            if ord(key[i]) >= 65 and ord(key[i]) <= 90:
                charKey = ord(key[i]) - 65
            elif ord(key[i]) >= 97 and ord(key[i]) <= 122:
                charKey = ord(key[i]) - 97
            result += chr(((charPt - charKey) % 26) + 65)
        elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            charPt = ord(ciphertext[i]) - 97
            if ord(key[i]) >= 65 and ord(key[i]) <= 90:
                charKey = ord(key[i]) - 65
            elif ord(key[i]) >= 97 and ord(key[i]) <= 122:
                charKey = ord(key[i]) - 97
            result += chr(((charPt - charKey) % 26) + 97)
    return result

def padding(text, key):
    temp = key
    while len(temp) < len(text):
        temp += key
    return temp

def menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key: ")
            print("Encrypted text:", encrypt(plaintext, key))
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            print("Decrypted text:", decrypt(ciphertext, key))
        elif choice == '3':
            print("Exiting program")
            break
        else:
            print("Invalid option. Please try again.")

menu()
