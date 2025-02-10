#  nano encrypt.py
def encrypt(text):
    encrypted = ''
    for char in text:
        encrypted += str(ord(char)) + ' '
    return encrypted.strip()

if __name__ == "__main__":
    original_text = "Saeid"
    encrypted_text = encrypt(original_text)
    print(f"Encrypted text: {encrypted_text}")
