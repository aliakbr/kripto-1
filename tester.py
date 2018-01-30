# """
#     This script used to be the main program
# """
from vigenere_alphabetic import Vigenere_Cypher


plain_text = "halo halo bandung!"
key = "sosro"

# vigenere = Vigenere_Cypher()
# encrypted = vigenere.encrypt(key, plain_text)
# decrypted = vigenere.decrypt(key, encrypted)
#
# print (plain_text)
# print (key)
# print (encrypted)
# print (decrypted)
#
from playfair_alphabetic import Playfair, search

playfair = Playfair(key)

matrix = playfair.matrix

for i in range(5):
    for j in range(5):
        print(matrix[i][j], end='')
    print("")

p_encryted = playfair.encrypt(plain_text)
print (p_encryted)
print (playfair.decrypt(p_encryted))
# a = 0
# a = input("Tes tes :")
# print (type(a))

# File Encrypt test
# list = []
# hh = []
# k = open('b.png', 'wb')
# with open('a.png','rb') as f1:
#    while True:
#       b = f1.read(1)
#       if b:
#          # process b if this is your intent
#         list.append(ord(b))
#         k.write(b)
#         hh.append(b)
#       else: break
# k.close()
#
# list = [hex(c).split('x')[-1] for c in list]
# for i,c in enumerate(list):
#     if len(c) == 1:
#         list[i] = '0'+c
#
# hex_string = ' '.join(list)
# print (hex_string)
# # from binascii import unhexlify
# # b = unhexlify(hex_string)
# result = bytes.fromhex(hex_string)
#
# with open('c.png', 'wb') as f2:
#     f2.write(result)

# # Ascii test
# from vigenere_ascii import Vigenere_Ascii
# plaintext = input("Input ascii character :")
# key = input("Input key :")
# vigenere_ascii = Vigenere_Ascii()
# plaintext = [c for c in plaintext]
# encrypted = vigenere_ascii.encrypt(key, plaintext)
# print (''.join(encrypted))
# decrypted = vigenere_ascii.decrypt(key, encrypted)
# print (''.join(decrypted))
