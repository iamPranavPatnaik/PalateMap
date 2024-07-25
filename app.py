import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
from evaluateMenu import MenuEvaluator

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def perform_ocr(filepath):
    # Placeholder for OCR function; implement as needed
    img = Image.open(filepath)
    text = pytesseract.image_to_string(img)
    return text

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            text = perform_ocr(filepath)
            return render_template('result.html', text=text, image_url=filepath)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Handle login logic here (e.g., authenticate user)
        return redirect(url_for('loggedin'))  # Redirect to loggedin page after login
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Handle registration logic here (e.g., create a new user)
        return redirect(url_for('loggedin'))  # Redirect to loggedin page after registration
    return render_template('register.html')

@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
