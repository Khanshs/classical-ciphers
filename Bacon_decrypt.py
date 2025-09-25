import os
import string

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

# Reverse mapping for decryption
# Tạo bảng đảo ngược để giải mã
reverse_bacon_table = {v: k for k, v in bacon_table.items()}

def decrypt_bacon(cipher: str) -> str:
    """
    Decrypt Bacon's Cipher using uppercase/lowercase letters.
    Giải mã mật mã Bacon dựa vào chữ hoa/thường.

    Rule:
    - Uppercase = A
    - Lowercase = B
    """
    result = []
    bacon_temp = ""
    # Remove spaces and punctuation / Xóa khoảng trắng và dấu câu
    ciphertext = cipher.replace(" ", "").translate(str.maketrans("", "", string.punctuation))

    for char in ciphertext:
        bacon_temp += 'A' if char.isupper() else 'B'
        if bacon_temp in reverse_bacon_table:
            result.append(reverse_bacon_table[bacon_temp])
            bacon_temp = ""
    return ''.join(result)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    if not os.path.exists(input_file):
        print(f"[!] File {input_file} not found / Không tìm thấy {input_file}")
        exit(1)

    decoded_lines = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                decoded_lines.append(decrypt_bacon(line))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(decoded_lines))

    print("[+] Done! Result saved to output.txt / Giải mã xong! Kết quả lưu trong output.txt")
    print("\n".join(decoded_lines))
