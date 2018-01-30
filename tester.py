# """
#     This script used to be the main program
# """
# from vigenere_alphabetic import Vigenere_Cypher
#
#
# plain_text = "hello world"
# key = "sosro"
#
# vigenere = Vigenere_Cypher()
# encrypted = vigenere.encrypt(key, plain_text)
# decrypted = vigenere.decrypt(key, encrypted)
#
# print (plain_text)
# print (key)
# print (encrypted)
# print (decrypted)
#
# from playfair_alphabetic import Playfair, search
#
# playfair = Playfair(key)
#
# matrix = playfair.matrix
#
# for i in range(5):
#     for j in range(5):
#         print(matrix[i][j], end='')
#     print("")
#
# p_encryted = playfair.encrypt(plain_text)
# print (p_encryted)
# print (playfair.decrypt(p_encryted))
# a = 0
# a = input("Tes tes :")
# print (type(a))

# File Encrypt test
# list = []
# with open('a.png','rb') as f1:
#    while True:
#       b = f1.read(1)
#       if b:
#          # process b if this is your intent
#         list.append(ord(b))
#       else: break
#
# print (list)
# print (len(list))

# Ascii test
from vigenere_ascii import Vigenere_Ascii
plaintext = input("Input ascii character :")
key = input("Input key :")
vigenere_ascii = Vigenere_Ascii()
plaintext = [c for c in plaintext]
encrypted = vigenere_ascii.encrypt(key, plaintext)
print (''.join(encrypted))
decrypted = vigenere_ascii.decrypt(key, encrypted)
print (''.join(decrypted))
