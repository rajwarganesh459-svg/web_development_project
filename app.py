from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import subprocess
import os

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DATABASE ----------------
def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT", 3306)),
        use_pure=True
    )

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- SIGNUP ----------------
@app.route('/signup', methods=['POST'])
def signup():
    try:
        db = get_db()
        cursor = db.cursor()

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor.execute(
            "INSERT INTO customer (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )

        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('home'))

    except Exception as e:
        return f"Signup Error: {str(e)}"
# ---------------- LOGIN ----------------
@app.route('/login', methods=['POST'])
def login():
    try:
        db = get_db()
        cursor = db.cursor()

        email = request.form['email']
        password = request.form['password']

        cursor.execute(
            "SELECT name FROM customer WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            session['user'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Login"

    except Exception as e:
        return f"Login Error: {str(e)}"
# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', name=session['user'])
    return redirect(url_for('home'))

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# ---------------- C++ JOB MATCHING ----------------
@app.route('/match', methods=['POST'])
def match():
    skills = request.form['skill']

    exe_file = './matcher' if os.name != 'nt' else 'matcher.exe'

    process = subprocess.Popen(
        [exe_file],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    output, _ = process.communicate(skills)

    return render_template('result.html', job=output)

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#print("DB_HOST:", os.getenv("DB_HOST"))
    
