"""
    Main Program
"""
from vigenere_alphabetic import Vigenere_Cypher, is_alphabet
from playfair_alphabetic import Playfair
from vigenere_ascii import Vigenere_Ascii

def output_5_gram(cipher):
    five_grams_cipher = []
    count = 0
    five_grams_word = ""
    for c in cipher:
        five_grams_word += c
        count += 1
        if count == 5:
            five_grams_cipher.append(five_grams_word)
            count = 0
            five_grams_word = ""
    if five_grams_word:
        five_grams_cipher.append(five_grams_word)
    return ' '.join(five_grams_cipher)

def output_as_plaintext(cipher, plaintext):
    output = ""
    i = 0
    for c in plaintext:
        if is_alphabet(c):
            output += cipher[i]
            i += 1
        else:
            output += " "
    return output

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
        print ("Your plaintext : {}".format(plaintext))
        print("Your encrypted message (raw): {}".format(result))
        # Print formatted ciphertext
        print ("Your encrypted message (in 5 gram) : {}".format(output_5_gram(result)))
        print ("Your encrypted message (same as plaintext) : {}".format(output_as_plaintext(result, plaintext)))
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
