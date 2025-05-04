# app.py
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename
from dataProcessing import *
from Threads import *
from flask import send_file
import time
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

script = ''

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['txt'])

# api = API(app)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CACHE_TYPE"] = "null"

# Add after app creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1221@localhost/hybrid_crypt_db'
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Add a proper secret key

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

def resultE():
    path = "./Segments"
    dir_list = os.listdir(path)
    print(dir_list)
    return render_template('Result.html',dir_list = dir_list)

def resultD():
    return render_template('resultD.html')

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))  # Changed from 128 to 200
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Add these routes before the existing ones
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
            
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
            
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('index'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/encrypt/')
@login_required  # Add this
def EncryptInput():
  Segment()
  gatherInfo()
  HybridCrypt()
  return resultE()

@app.route('/decrypt/')
@login_required  # Add this
def DecryptMessage():
  st=time.time()
  HybridDeCrypt()
  et=time.time()
  print(et-st)
  trim()  # Call the modified trim function
  st=time.time()
  Merge()
  et=time.time()
  print(et-st)
  return resultD()

def start():
  content = open('./Original.txt','r')
  content.seek(0)
  first_char = content.read(1) 
  if not first_char:
    return render_template('Empty.html')
  else:
    return render_template('Option.html')

@app.route('/')
def index():
  return render_template('index.html')

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/return-files-key/')
def return_files_key():
    try:
        return send_file('./Original.txt', download_name='Original.txt', as_attachment=True)
    except Exception as e:
        return str(e)
    
@app.route('/return-files-data/')
def return_files_data():
    try:
        return send_file('./Output.txt', download_name='Output.txt', as_attachment=True)
    except Exception as e:
        return str(e)


@app.route('/data/', methods=['GET', 'POST'])
@login_required  # Add this
def upload_file():
  if request.method == 'POST':
    if 'file' not in request.files:
      return render_template('Nofile.html')
    file = request.files['file']
    if file.filename == '':
      return render_template('Nofile.html')
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Original.txt'))
      return start()
       
    return render_template('Invalid.html')
    
if __name__ == '__main__':
  app.run(debug=True)

# Modified trim function
def trim():
    with open('./Output.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    # Rest of the function code
