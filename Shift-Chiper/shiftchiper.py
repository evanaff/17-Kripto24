# Shift Chiper - Affine Chiper

def encrypt(a,b,plaintext):
    result = ""
    for c in plaintext:
        if ord(c) >= 65 and ord(c) <= 90:
            abjad = ord(c) - 65
            enc = chr((a*abjad + b) % 26 + 65)
        elif ord(c) >= 97 and ord(c) <= 122:
            abjad = ord(c) - 97
            enc = chr((a*abjad + b) % 26 + 97)
        else:
            enc = c        
        result += enc
    return result

def decrypt(a,b,chipertext):
    result = ""
    for c in chipertext:
        if ord(c) >= 65 and ord(c) <= 90:
            abjad = ord(c) - 65
            dec = chr(int(pow(a,-1,26)*(abjad - b) % 26 + 65))
        elif ord(c) >= 97 and ord(c) <= 122:
            abjad = ord(c) - 97
            dec = chr(int(pow(a,-1,26)*(abjad - b) % 26 + 97))
        else:
            dec = c        
        result += dec
    return result

def encryptFile(a,b,input_file,output_file):
    with open(input_file, 'r') as input, open(output_file, 'w') as output:
        for line in input:
            output.write(encrypt(a,b,line))

def decryptFile(a,b,input_file,output_file):
    with open(input_file, 'r') as input, open(output_file, 'w') as output:
        for line in input:
            output.write(decrypt(a,b,line))

def mainMenu():
    print("\n======================= AFFINE CHIPER PROGRAM =======================")
    print("1. Encrypt")
    print("2. Decrypt")
    print("0. Exit")
    choice = input("Select menu : ")
    return choice

def inputMenu(type):
    if type == "encrypt":
        title = "ENCRYPT"
        menu = "Plaintext"
    elif type == "decrypt":
        title = "DECRYPT"
        menu = "Chipertext"
    print(f"\n======================= {title} MENU =======================")
    print(f"1. Input {menu}")
    print("2. Input File")
    print("0. Back")
    choice = input("Select menu : ")
    return choice

check =  True

while check == True:
    choice = mainMenu()
    match choice:
        case "1":
            check2 = True
            while check2 == True:
                choice2 = inputMenu("encrypt")
                match choice2:
                    case "1":
                        a = int(input("a : "))
                        b = int(input("b : "))
                        pt = input("Plaintext : ")
                        print(f"Encryption Result = {encrypt(a,b,pt)}")
                        check2 = False
                    case "2": 
                        a = int(input("a : "))
                        b = int(input("b : "))
                        input_file = input("Input File Name : ")
                        output_file = input("Output File Name : ")
                        encryptFile(a,b,input_file,output_file)
                        print(f"Encryption Result in {output_file}")
                        check2 = False
                    case "0":
                        check2 =  False
                    case _:
                        print("Incorrect Input!!")
        case "2":
            check2 = True
            while check2 == True:
                choice2 = inputMenu("decrypt")
                match choice2:
                    case "1":
                        a = int(input("a : "))
                        b = int(input("b : "))
                        pt = input("Chipertext : ")
                        print(f"Decryption Result = {decrypt(a,b,pt)}")
                        check2 = False
                    case "2": 
                        a = int(input("a : "))
                        b = int(input("b : "))
                        input_file = input("Input File Name : ")
                        output_file = input("Output File Name : ")
                        decryptFile(a,b,input_file,output_file)
                        print(f"Decryption Result in {output_file}")
                        check2 = False
                    case "0":
                        check2 = False
                    case _:
                        print("Incorrect Input!!")
        case "0":
            check = False
        case _:
            print("Incorrect Input!!")
    