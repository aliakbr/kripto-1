"""
    This script used to be the main program
"""
from vigenere_cypher import Vigenere_Cypher

vigenere = Vigenere_Cypher()

plain_text = "hello world"
key = "sosro"
encrypted = vigenere.encrypt(key, plain_text)
decrypted = vigenere.decrypt(key, encrypted)

print (plain_text)
print (key)
print (encrypted)
print (decrypted)
