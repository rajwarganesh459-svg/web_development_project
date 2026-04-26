from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import subprocess
import os

app = Flask(__name__)
app.secret_key = "secret123"

# Database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="ganesh",
    password="123Ganesh",
    database="job_portal"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

# Signup
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    cursor.execute(
        "INSERT INTO customer (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    db.commit()

    return redirect(url_for('home'))

# Login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cursor.execute(
        "SELECT * FROM customer WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        session['user'] = user[2]
        return redirect(url_for('dashboard'))
    else:
        return "Invalid Login"

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', name=session['user'])
    return redirect(url_for('home'))

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# Job Matching (C++)
@app.route('/match', methods=['POST'])
def match():
    skills = request.form['skill']
    if os.name == 'nt':  # Windows
        exe_file = 'matcher.exe'
    else:  # Linux
        exe_file = './matcher'
    process = subprocess.Popen(
    [exe_file],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True)


    output, _ = process.communicate(skills)

    return render_template('result.html', job=output)

app.run(debug=True)