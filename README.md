## 📌 Overview

A full-stack **Job Portal Full Stack Web Application with Skill-Based Matching** that allows users to:

* Register and login securely
* Access a personalized dashboard
* Enter skills and receive job recommendations
* Experience fast matching powered by a **C++ backend engine**

This project demonstrates integration of **Python (Flask), MySQL, and C++** in a real-world deployment.

---

## 🌐 Live Demo

Demo

👉 https://skilllbased-job-matching-portal-3.onrender.com

---

## 🛠️ Tech Stack

| Layer        | Technology     |
| ------------ | -------------- |
| Backend      | Flask (Python) |
| Database     | MySQL          |
| Frontend     | HTML, CSS      |
| Logic Engine | C++            |
| Deployment   | Render         |

---

## ⚙️ Features

* 🔐 User Authentication (Signup/Login)
* 📊 Dashboard with session handling
* 💾 MySQL Database Integration
* ⚡ Fast job matching via C++ executable
* 🌍 Live deployment on Render

---

## 🧠 System Workflow

User Input (Skills)
        ↓
Flask Backend
        ↓
C++ Matching Engine
        ↓
Processed Output
        ↓
Displayed on Web UI

## 🗂️ Project Structure

WebProject/
│── app.py
│── matcher.cpp
│── build.sh
│── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── result.html
│
├── static/
│   └── style.css

## ▶️ Run Locally

### 1. Clone Repository

git clone https://github.com/rajwarganesh459-svg/skilllBased_job_Matching_portal
cd web_development_project

### 2. Install Dependencies

pip install -r requirements.txt


### 3. Compile C++ Code

g++ matcher.cpp -o matcher

### 4. Configure Environment Variables

DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
DB_PORT=3306

### 5. Run Application

python app.py


Open

http://localhost:5000


## ⚠️ Important Notes

* Ensure `customer` table exists in MySQL
* C++ compiler (g++) must be installed
* Environment variables must be correctly configured

---

## 🚀 Future Enhancements

* 🔒 Password hashing (security improvement)
* 📈 Multiple job recommendations
* 🎨 UI/UX improvements
* 🔑 JWT Authentication
* 📡 REST API integration

---

## 👨‍💻 Author

**Ganesh Rajwar**

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
