def decrypt(encrypted_text):
    decrypted = ''
    for num in encrypted_text.split():
        decrypted += chr(int(num))
    return decrypted

if __name__ == "__main__":
    encrypted_text = input("Please enter the text to decrypt (numbers separated by spaces): ")
    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted text: {decrypted_text}")
