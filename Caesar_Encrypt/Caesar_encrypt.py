import os
import string
os.chdir(os.path.dirname(os.path.abspath(__file__)))
alphabet = string.ascii_uppercase 
# creating a aphabet conntaining both uppercase and lowercase letters



def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char in alphabet:
            index = (alphabet.index(char) + key) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += char
    return ciphertext



if __name__ == "__main__":        
    with open('Caesar.INP', 'r') as f:
        key = int(f.readline().strip())
        plaintext = f.readline().strip()
        if key < 0 or key > 25:
            raise ValueError("Key must be between 0 and 25")
        #raise error if key is not in the range 0-25
        print(f"Key: {key}")
        print(f"Plaintext: {plaintext}")
        
    with open('Caesar.OUT', 'w') as f:
        ciphertext = caesar_encrypt(plaintext, key)
        f.write(ciphertext + '\n')
        print("Ciphertext written to Caesar.OUT")
        
    
    

