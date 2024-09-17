import numpy as np

def inputKey(key_length):
    key = np.zeros((key_length, key_length), dtype=int)
    print("Input Key Matrix")
    for i in range(key_length):
        for j in range(key_length):
            key[i][j] = int(input(f"({i}, {j}) : "))
    key = np.array(key)
    print("Key Matrix : ")
    print(key)
    return key

def validateKey(key):
    determinant = int(np.round(np.linalg.det(key)))
    if np.gcd(determinant, 26) == 1:
        return True
    else:
        return False

def textMatrix(pt, key_length):
    text_matrix = []
    for c in pt:
        if c.isalpha():
            text_matrix.append(ord(c.upper()) - 65)
    while len(text_matrix) % key_length != 0:
        text_matrix.append(ord('x') - 97)
    text_matrix = np.array(text_matrix).reshape(-1, key_length)
    return text_matrix

def encrypt(pt, pt_matrix, key):
    chipertext = ""
    index = 0
    for row in pt_matrix:
        matrix = np.array(row).reshape(-1, 1)
        result = np.matmul(key, matrix).flatten()
        for i in result:
            if pt[index].isupper():
                chipertext += chr(i%26 + 65)
            else:
                chipertext += chr(i%26 + 97)
            index += 1
    return chipertext

def det2x2(matrix):
    return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

def cofactor_matrix(matrix):
    cofactors = np.zeros((3, 3))
    for row in range(3):
        for col in range(3):
            submatrix = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
            sign = (-1) ** (row + col)  
            cofactors[row, col] = sign * det2x2(submatrix)
    return cofactors

def adjugate_matrix_3x3(matrix):
    cofactors = cofactor_matrix(matrix)
    adjugate = cofactors.T  
    return adjugate

def modularInverse(matrix, key_length):
    determinant = int(np.round(np.linalg.det(matrix))) % 26
    det_inverse = pow(determinant, -1, 26)
    if key_length == 2:
        a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
        adj_mod = np.array([[d, -b], [-c, a]]) % 26
    elif key_length == 3:
        adj_mod = adjugate_matrix_3x3(matrix) % 26
    return det_inverse*adj_mod

def decrypt(ct, ct_matrix, key, key_length):
    plaintext = ""
    index = 0
    inv_key = modularInverse(key, key_length)
    for row in ct_matrix:
        matrix = np.array(row).reshape(-1, 1)
        result = np.matmul(inv_key, matrix).flatten()
        for i in result:
            i = int(np.round(i))
            if ct[index].isupper():
                plaintext += chr(i%26 + 65)
            else:
                plaintext += chr(i%26 + 97)
            index += 1
    return plaintext

def findKey(pt, ct, key_length):
    if len(pt) != len(ct):
        print("Plaintext and Ciphertext doesn't has same length!")
        return 0
    check = True
    key = None
    while len(pt) > 3 and check == True:
        pt_chunk = pt[:4]
        ct_chunk = ct[:4]
        pt = pt[2:]
        ct = ct[2:]
        pt_matrix =  textMatrix(pt_chunk, 2).flatten()
        ct_matrix =  textMatrix(ct_chunk, 2).flatten()
        pt_matrix2 = np.zeros((2,2), dtype=int)
        ct_matrix2 = np.zeros((2,2), dtype=int)
        index = 0
        for i in range(2):
            for j in range(2):
                pt_matrix2[j, i] = pt_matrix[index]
                ct_matrix2[j, i] = ct_matrix[index]
                index += 1
        if validateKey(pt_matrix2):
            pt_inv = modularInverse(pt_matrix2, key_length) 
            key = np.matmul(ct_matrix2, pt_inv) % 26
            check = False
    if check == True:
        print("Cannot find key : There is no combination of plaintext matrix that invertible to modulo 26")
    return key
    
def menu():
    print("\n======================== HILL CIPHER ========================")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Find Key (2x2)")
    print("0. Exit")
    return input("Select : ")

check = True
while check:
    select = menu()
    match select:
        case "1":
            pt = input("Plaintext : ")
            key_check = False
            while key_check == False:
                key_length = input("Key Length (2 or 3) : ")
                if key_length == "2" or key_length == "3":
                    key_length = int(key_length)
                    if key_length <= len(pt):
                        key_check = True
                    else:
                        print("Key is too long for plaintext")    
                else:
                    print("Invalid key length!")
            key_check = False
            while key_check == False:
                key = inputKey(key_length)
                if validateKey(key):
                    key_check = True
                else:
                    print("Key Matrix is not invertible with modulo 26")
            pt_matrix = textMatrix(pt, key_length)
            ct = encrypt(pt, pt_matrix, key)
            print(f"Ciphertext : {ct}")
        case "2":
            ct = input("Ciphertext : ")
            key_check = False
            while key_check == False:
                key_length = input("Key Length (2 or 3) : ")
                if key_length == "2" or key_length == "3":
                    key_length = int(key_length)
                    if key_length <= len(ct):
                        key_check = True
                    else:
                        print("Key is too long for ciphertext")  
                else:
                    print("Invalid key length!")
            key_check = False
            while key_check == False:
                key = inputKey(key_length)
                if validateKey(key):
                    key_check = True
                else:
                    print("Key Matrix is not invertible with modulo 26")
            ct_matrix = textMatrix(ct, key_length)
            ct = decrypt(ct, ct_matrix, key, key_length)
            print(f"Plaintext : {ct}")
        case "3":
            pt = input("Input Plaintext : ")
            ct = input("Input Ciphertext : ")
            print(f"Recovered Key : \n{findKey(pt, ct, 2)}")
        case "0":
            check = False
        case _:
            print("Invalid Input!!")

