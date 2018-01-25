"""
    Script for alphabetic vigenere
"""

ASCII_BASE = 97

def is_alphabet(character):
    """
        Return true if the character is alphabet in lowercase
        and return false otherwise
    """
    return (ord(character) >= 97 and ord(character) <= 122)

def padd_key(key, plaintext):
    """
        Input :
            key : Key of the vigenere algorithm
            plaintext : Plain Text
        Output :
            string of padded key
    """
    pad_len = len(plaintext) - len(key)
    j = 0  #index of key
    output = key
    for i in range(pad_len):
        if (is_alphabet(plaintext[i + len(key)])):
            output += key[j]
            j += 1
            if (j == len(key)):
                j = 0
        else:
            output += plaintext[i + len(key)]
    return output


class Vigenere_Cypher:
    """
        Vigenere Alphabetic Class
    """
    def encrypt(self, key, plaintext):
        """
            This function will return ciphertext of the plain Text
            Input :
                key : Key string
                plaintext : Plain Text
            Output :
                string of encrypted string
        """
        output = ""
        padded_key = padd_key(key, plaintext)
        for i in range(len(plaintext)):
            if is_alphabet(plaintext[i]):
                enc_ascii = ((ord(plaintext[i]) + ord(padded_key[i]) - 2*ASCII_BASE) % 26) + ASCII_BASE
                output += chr(enc_ascii)
        return output

    def decrypt(self, key, encrypted):
        """
            This function will return decrypted text
            Input :
                key : Key string
                encrypted_txt : encrypted string
            Output :
                decrypted string
        """
        output = ""
        padded_key = padd_key(key, encrypted)
        for i in range(len(encrypted)):
            if is_alphabet(encrypted[i]):
                dec_ascii = ((ord(encrypted[i]) - ord(padded_key[i])) % 26) + ASCII_BASE
                output += chr(dec_ascii)
        return output
