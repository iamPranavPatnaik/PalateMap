import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
from evaluateMenu import MenuEvaluator
from readMenu import ReadMenu
import firebase_admin
from firebase_admin import credentials, auth

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize Firebase Admin SDK
cred = credentials.Certificate('palatemapfirebase.json')
firebase_admin.initialize_app(cred)

# No way ts works
app.secret_key = os.urandom(24)  # Generates a random key

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
            readMenu = ReadMenu()
            # user_menu = readMenu.parseMenu(menu)
            eval_menu = MenuEvaluator()
            dish_vectors = eval_menu.evaluate_menu(filepath)
            return render_template('result.html', text=dish_vectors, image_url=filepath) # CHANGE THIS CHANGE THIS CHANGE THIS
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            if not email:
                raise ValueError("Email is required.")
            if not password:
                raise ValueError("Password is required.")
            
            user = auth.get_user_by_email(email)
            flash("Login successful!", "success")
            return redirect(url_for('loggedin'))  # Redirect to loggedin page after login
        
        except ValueError as ve:
            flash(f"Input Error: {str(ve)}", "danger")

        except firebase_admin._auth_utils.UserNotFoundError:
            flash("No user record found for the provided email.", "danger")

        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Email and password are required.", "danger")
            return redirect(url_for('register'))

        # Handle registration logic here (e.g., create a new user)
        try:
            user = auth.create_user(email=email, password=password)
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except firebase_admin.auth.EmailAlreadyExistsError:
            flash("Email already in use.", "danger")
        except Exception as e:
            flash(f"Registration failed: {str(e)}", "danger")
    return render_template('register.html')

@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
