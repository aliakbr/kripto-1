"""
    Main Program
"""
from vigenere_alphabetic import Vigenere_Cypher
from playfair_alphabetic import Playfair, search

print ("Welcome to Kripto 1!")
print ("Choose your option!")
print("1. Encrypt")
print("2. Decrypt")
opt = 0
in_opt = 0
alg_opt = 0
while opt != 1 and opt != 2:
    opt = int(input("Input :"))

if opt == 1:
    print ("Input your plaintext")
    print ("1. File")
    print ("2. Standard Input")
    while in_opt != 1 and in_opt != 2:
        in_opt = int(input("Enter your option :"))
    if in_opt == 1:
        input_text = input("Enter text file :")
        plaintext = open(input_text, "r")
    else:
        input_text = input("Enter plaintext :")

    key = input("Enter the key :")

    print ("Choose your algorithm")
    print ("1. Vigenere Cipher")
    print ("2. Playfair Cipher")
    while alg_opt != 1 and alg_opt != 2:
        alg_opt = int(input("Input :"))
    if alg_opt == 1:
        vigenere = Vigenere_Cypher()
        encrypted = vigenere.encrypt(key, input_text)
    else:
        playfair = Playfair(key)
        encryted = playfair.encrypt(input_text)
    print ("Encrypted Message : {}".format(encrypted))
else:
    print ("Input your ciphertext")
    print ("1. File")
    print ("2. Standard Input")
    while in_opt != 1 and in_opt != 2:
        in_opt = int(input("Enter your option :"))
    if in_opt == 1:
        input_text = input("Enter text file :")
        cipher_text = open(input_text, "r")
    else:
        cipher_text = input("Enter cipher:")

    key = input("Enter the key :")

    print ("Choose your algorithm")
    print ("1. Vigenere Cipher")
    print ("2. Playfair Cipher")
    while alg_opt != 1 and alg_opt != 2:
        alg_opt = int(input("Input :"))
    if alg_opt == 1:
        vigenere = Vigenere_Cypher()
        decrypted = vigenere.decrypt(key, cipher_text)
    else:
        playfair = Playfair(key)
        decrypted = playfair.encrypt(cipher_text)
    print ("Decrypted Message : {}".format(decrypted))
