"""
    Main Program
"""
from vigenere_alphabetic import Vigenere_Cypher
from playfair_alphabetic import Playfair
from vigenere_ascii import Vigenere_Ascii

print ("Welcome to Kripto-1!")
print ("Choose your option!")
print("1. Encrypt")
print("2. Decrypt")
opt = 0
while not (opt == 1 or opt == 2):
    opt = int(input("Input your option :"))

print ("Choose your input option")
print ("1. Text File")
print ("2. Raw Input")
print ("3. File")

input_opt = 0
while not (input_opt == 1 or input_opt == 2 or input_opt == 3):
    input_opt = int(input("Input your option :"))
plain_in = input("Input your text/filename :")
key = input("Input your key :")

print ("Choose algorithm")
print ("1. Vigenere (Alphabetic)")
print ("2. Vigenere (ASCII)")
print ("3. Playfair (Alphabetic)")
alg_opt = 0

if input_opt == 3:
    while alg_opt != 2:
        alg_opt = int(input("Input your option (Only Vigenere ASCII available for this input) :"))
else:
    while not (alg_opt == 1 or alg_opt == 2 or alg_opt == 3):
        alg_opt = int(input("Input your option :"))

if input_opt == 1:
    with open(plain_in, "r") as f:
        plaintext = f.read()
elif input_opt == 2:
    plaintext = plain_in
else:
    plaintext = []
    with open(plain_in,'rb') as f1:
       while True:
          b = f1.read(1)
          if b:
              plaintext.append(chr(ord(b)))
          else: break

# Encryption/Decryption process
vigenere = Vigenere_Cypher()
vigenere_ascii = Vigenere_Ascii()
playfair = Playfair(key)
if opt == 1:
    if alg_opt == 1:
        print (plain_in)
        result = vigenere.encrypt(key, plaintext)
    elif alg_opt == 2:
        result = ''.join(vigenere_ascii.encrypt(key, plaintext))
    else:
        result = playfair.encrypt(plaintext)
else:
    if alg_opt == 1:
        result = vigenere.decrypt(key, plaintext)
    elif alg_opt == 2:
        result = ''.join(vigenere_ascii.decrypt(key, plaintext))
    else:
        result = playfair.decrypt(plaintext)

if input_opt != 3:
    if opt == 1:
        print("Your encrypted message : {}".format(result))
    else:
        print ("Your decrypted message : {}".format(result))

savefile = input("Input your output filename :")
if input_opt == 3:
    list_hex = [hex(ord(c)).split('x')[-1] for c in result]
    for i, c in enumerate(list_hex):
        if len(c) == 1:
            list_hex[i] = '0'+c
    hex_string = ' '.join(list_hex)
    bytes_result = bytes.fromhex(hex_string)
    with open(savefile, 'wb') as f:
        f.write(bytes_result)
else:
    with open(savefile, 'w') as f:
        f.write(result)
