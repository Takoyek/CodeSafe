from flask import Flask, request, render_template_string

app = Flask(__name__)

def encrypt(text):
    encrypted = ''.join(str(ord(char)) + ' ' for char in text).strip()
    return encrypted

def decrypt(encrypted_text):
    decrypted = ''.join(chr(int(num)) for num in encrypted_text.split())
    return decrypted

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']
        if action == 'encrypt':
            result = encrypt(text)
        elif action == 'decrypt':
            result = decrypt(text)
        return render_template_string(TEMPLATE, result=result)
    return render_template_string(TEMPLATE)

TEMPLATE = '''
<!doctype html>
<html>
<head><title>Encryption and Decryption</