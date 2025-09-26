# 🔐 Caesar Cipher (Encryption & Decryption)

This folder contains Python scripts to **encrypt** and **decrypt** messages using the classical **Caesar Cipher**, shifting letters by a fixed key.

## 📂 Files

- `caesar_encrypt.py` → Reads a numeric key and plaintext from `Caesar.INP`, outputs ciphertext to `Caesar.OUT`.  
- `caesar_decrypt.py` → Reads ciphertext from `Caesar.INP`, tries all 25 shifts, writes each plaintext candidate to `Caesar.OUT`.  

---

## 🚀 Usage

### 1. Encryption

1. In `Caesar.INP`, put:
   ```text
   5
   HELLO WORLD
   ```
2. Run:
   ```bash
   python caesar_encrypt.py
   ```
3. Check `Caesar.OUT`:
   ```text
   MJQQT BTWQI
   ```

---

### 2. Decryption

1. In `Caesar.INP`, put your ciphertext:
   ```text
   MJQQT BTWQI
   ```
2. Run:
   ```bash
   python caesar_decrypt.py
   ```
3. Check `Caesar.OUT`:
   ```text
   Key  1   :   LIPPS ASVPH
   Key  2   :   KHOOR ZRUOG
   …
   Key 25   :   NKRRU CXARR
   ```

---

## ⚠️ Important Note

Both scripts use the same filenames:

- **Input:** `Caesar.INP`  
- **Output:** `Caesar.OUT`  

Each run overwrites `Caesar.OUT`. To decrypt after encrypting, copy the ciphertext from `Caesar.OUT` back into `Caesar.INP`.

---

## 🧾 Notes

- Only uppercase alphabet letters are shifted; other characters remain unchanged.  
- Encryption converts plaintext to uppercase before shifting.  
- Valid keys: 0–25; values outside this range raise an error.

---

## 🔭 Next Steps

- Automate best-plaintext selection via English-frequency scoring.  
- Preserve original letter casing during shifts.  
- Add `argparse` CLI support for custom filenames and direct input.  
- Explore ROT13 or other shift ciphers as special cases.
