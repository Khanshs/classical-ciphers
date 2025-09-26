import os
import string
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def caesar_decrypt(ciphertext):
    alphabet = string.ascii_uppercase
    results = []
    for key in range(1, 26):
        decrypted_chars = []
        for char in ciphertext.upper():
            if char in alphabet:
                #index is the position of char in the alphabet
                #the main logic of decryption is to shift the index back by key positions
                index = (alphabet.index(char) - key) % 26
                decrypted_chars.append(alphabet[index])
            else:
                decrypted_chars.append(char)
        plaintext = ''.join(decrypted_chars)
        results.append((key, plaintext))
    return results

if __name__ == '__main__':
    # Ensure script works from its own directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Read the ciphertext
    with open('Caesar.INP', 'r') as infile:
        ciphertext = infile.readline().strip()

    # Decrypt with every possible shift
    decrypted_versions = caesar_decrypt(ciphertext)

    # Write each shift attempt to the output file
    with open('Caesar.OUT', 'w') as outfile:
        for key, plaintext in decrypted_versions:
            # Format key to be right-aligned in a field of width 2 (newthings learned)
            outfile.write(f'Key {key:2d}   :   {plaintext}\n')
    print("Decryption attempts written to Caesar.OUT")
# Ensure script works from its own directory
