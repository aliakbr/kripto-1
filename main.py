"""
    This script used to be the main program
"""
from vigenere_alphabetic import Vigenere_Cypher


plain_text = "hello world"
key = "sosro"

vigenere = Vigenere_Cypher()
encrypted = vigenere.encrypt(key, plain_text)
decrypted = vigenere.decrypt(key, encrypted)

print (plain_text)
print (key)
print (encrypted)
print (decrypted)

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
