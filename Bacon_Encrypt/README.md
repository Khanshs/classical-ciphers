# 🔐 Bacon Cipher (Encryption & Decryption)

This folder contains Python scripts to **encrypt** and **decrypt** messages using the classical **Bacon Cipher**, where uppercase = `A` and lowercase = `B`.

## 📂 Files
- `Bacon_encrypt.py` → Encrypts plaintext into Bacon cipher (output text with uppercase/lowercase patterns).  
- `Bacon_decrypt.py` → Decrypts text back to plaintext.  

## 🚀 Usage

### 1. Encryption
Put your plaintext message in `input.txt`, for example:
    Hello World
Run:
```bash
python Bacon_encrypt.py
```
Result will be saved in `output.txt`, e.g.:
    `CHoqn ENeSX WuAxl QbXhx SkgaW   hGpfQ NdkcN fXPJr YvQtj QHDsy`
  
### 2. Decryption
Put your ciphertext (with uppercase/lowercase patterns) in `input.txt`, 
for example:
    I WENt TO SCHOOL tODay, iT Was RaInING nO I dO NOt lIKe it WHen iT RAIns
Run:
```bash
python Bacon_decrypt.py
```
Result will be saved in `output.txt`: 
    `BACONISGOOD`

## ⚠️ Important Note

Both scripts use the same filenames:

- **Input file:** `input.txt`  
- **Output file:** `output.txt`  

👉 This means:
- After encrypting, if you want to decrypt, you must copy the ciphertext from `output.txt` back into `input.txt`.  
- Similarly, each run will **overwrite** the previous `output.txt`.  

💡 *(If you want to avoid this, rename files manually or edit the scripts to use different input/output filenames.)*

---

## 🧾 Notes
- Only alphabetic characters are encoded.  
- Spaces and punctuation marks are preserved.  
- The encryption uses random letter substitution, so the ciphertext may vary each time.  
