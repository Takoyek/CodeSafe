from flask import Flask, request, render_template, redirect, url_for, jsonify
from encrypt import encrypt
from decrypt import decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/main', methods=['POST'])
def main_page():
    password = request.form.get('password')
    if password == 'msi':
        return render_template('index.html')
    else:
        return redirect(url_for('index'))

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    text = request.form['text']
    encrypted = encrypt(text)
    return jsonify(result=encrypted)

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    text = request.form['text']
    decrypted = decrypt(text)
    return jsonify(result=decrypted)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
