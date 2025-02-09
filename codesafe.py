#  nano codesafe.py
from flask import Flask, request, render_template, redirect, url_for
import os
from encrypt import encrypt
from decrypt import decrypt
from functools import wraps
from flask import Flask, request, render_template, redirect, url_for, Response

app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == '0098'

def authenticate():
    return Response(
        'Please log in', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
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
    return render_template('result.html', result=encrypted, title='Encrypted')

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    text = request.form['text']
    decrypted = decrypt(text)
    return render_template('result.html', result=decrypted, title='Decrypted')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
