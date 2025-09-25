# Bacon_encrypt.py
import os
import string
import random
from string import ascii_lowercase, ascii_uppercase 

# Bacon cipher table (26 English letters)
# Bảng mã Bacon (26 chữ cái tiếng Anh)
bacon_table = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
    'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
    'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
    'Z': 'BBAAB'
}

def encrypt_bacon(message: str) -> str:
    """Mã hóa plaintext bằng Bacon cipher, trả về hoa/thường pattern"""
    result = []
    for char in message.upper():
        if char.isalpha():
            # Lấy mã A/B cho ký tự
            code = bacon_table[char]
            # A -> uppercase, B -> lowercase, ngẫu nhiên chọn chữ cái từ A-Z hoặc a-z rồi thêm khoảng cách cho đẹp 
            word = ''.join(random.choice(ascii_uppercase) if c == 'A' else random.choice(ascii_lowercase) for c in code)
            result.append(word)
        else:
            result.append(char)  # giữ nguyên khoảng trắng, dấu câu
    return ' '.join(result)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read().strip()

    cipher = encrypt_bacon(data)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(cipher)

    print("Encrypted:")
    print(cipher)
