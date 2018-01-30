"""
    A Script for Playfair algorithm implementation
"""
import re

# Built in function to search character in matrix
def search(matrix, char):
    """
        Search char in the matrix
        Return boolean
    """
    for x in matrix:
        for c in x:
            if c == char:
                return True
                break
    return False

def search_index(matrix, char):
    """
        Search char in the matrix
        Return index
    """
    row, col = -1, -1  # Default output if false
    for i, x in enumerate(matrix):
        for j, c in enumerate(x):
            if c == char:
                row, col = i, j
                break
    return row, col

def create_bigram_string(plaintext):
    """
        Create string consist of bigram
    """
    plaintext = re.sub(r'[^a-zA-Z]', r'', plaintext)
    plaintext = plaintext.replace('j', 'i')
    bigram_str = ""
    prev_char = ""
    for i, c in enumerate(plaintext):
        if not prev_char:
            bigram_str += c
            prev_char = c
        else:
            if prev_char != c:
                if i == len(plaintext) - 1 :
                    bigram_str += c
                else:
                    bigram_str += c + " "
                prev_char = ""
            else:
                bigram_str += 'z '  # Put Z if we found 2 same character
                bigram_str += c
                prev_char = c

    # Add extra z if it's odd
    if prev_char:
        bigram_str += 'z'
    return bigram_str

class Playfair:
    """
        Playfair algorithm class
        Assumption : replacing "J" with "I"
    """
    def __init__(self, keyword):
        # Init keyword
        self.keyword = keyword.lower()

        # Init table
        w, h = 5, 5
        self.matrix = [['A' for x in range(w)] for x in range(h)]
        keyword_words = ""
        for i in range(len(keyword)):
            if keyword[i] not in keyword_words:
                keyword_words += keyword[i]


        i, j = 0, 0 # table iterator

        # Fill table with keyword
        exit = False
        for w in keyword_words:
            if w != 'j':
                self.matrix[i][j] = w
                j += 1
                if (j == 5):
                    i += 1
                    j = 0
                    if (i == 5):
                        break
                        exit = True

        if not (exit):
            # Removing 'J' or 'Q'
            alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
            alphabet.remove('j')

            # Fill with alphabethic
            k = 0
            while i < 5:
                while j < 5:
                    if not search(self.matrix, alphabet[k]):
                        self.matrix[i][j] = alphabet[k]
                        j += 1
                    k += 1
                j = 0
                i += 1

    def encrypt(self, plaintext):
        """
            Encrypt plaintext with keyword
        """
        bigram_str = create_bigram_string(plaintext)
        print (bigram_str)

        # Encryption process
        encrypted = ""
        list_tup = bigram_str.split(' ')
        for tup in list_tup:
            i1, j1 = search_index(self.matrix, tup[0])
            i2, j2 = search_index(self.matrix, tup[1])

            if i1 == i2:
                if (j1 + 1) == 5:
                    j1 = 0
                else:
                    j1 += 1
                if (j2 + 1) == 5:
                    j2 = 0
                else:
                    j2 += 1
                encrypted += self.matrix[i1][j1]
                encrypted += self.matrix[i2][j2]
            elif j1 == j2:
                if (i1 + 1) == 5:
                    i1 = 0
                else:
                    i1 += 1
                if (i2 + 1) == 5:
                    i2 = 0
                else:
                    i2 += 1
                encrypted += self.matrix[i1][j1]
                encrypted += self.matrix[i2][j2]
            else:
                encrypted += self.matrix[i1][j2]
                encrypted += self.matrix[i2][j1]
        return encrypted

    def decrypt(self, encrypted):
        """
            Decrypt encrypted message to a plain text
            Input : Encrypted message
            Output : Plaintext
        """
        bigram_str = create_bigram_string(encrypted)

        # Decryption process
        decrypted = ""
        list_tup = bigram_str.split(' ')
        print (bigram_str)
        for tup in list_tup:
            i1, j1 = search_index(self.matrix, tup[0])
            i2, j2 = search_index(self.matrix, tup[1])

            if i1 == i2:
                if (j1 - 1) < 0:
                    j1 = 4
                else:
                    j1 -= 1
                if (j2 - 1) < 0:
                    j2 = 4
                else:
                    j2 -= 1
                decrypted += self.matrix[i1][j1]
                decrypted += self.matrix[i2][j2]
            elif j1 == j2:
                if (i1 - 1) == 0:
                    i1 = 4
                else:
                    i1 -= 1
                if (i2 + 1) == 5:
                    i2 = 4
                else:
                    i2 -= 1
                decrypted += self.matrix[i1][j1]
                decrypted += self.matrix[i2][j2]
            else:
                decrypted += self.matrix[i1][j2]
                decrypted += self.matrix[i2][j1]
        return decrypted
