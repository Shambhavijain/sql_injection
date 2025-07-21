# Vulnerable Voting App — SQL Injection Demonstration

## ❗ Purpose

This project demonstrates how a simple voting application built with Python (Flask) can be vulnerable to **SQL Injection attacks** when user inputs are not properly sanitized or validated.  
The goal is to raise awareness about common web security flaws and emphasize the importance of **input validation** and **safe coding practices**.

---

## 👤 Created By

**Shambhavi Jain**

This is the first project under **WatchGuard**, a company I founded to explore and showcase cybersecurity vulnerabilities in web applications.  
This demonstration project highlights the real-world risks of insecure coding practices by simulating a vulnerable voting system.

---

## 🖼️ Architecture Overview

This is a deliberately insecure system that:

- Accepts vote form input and places it directly into unsafe SQL queries.
- Allows attackers to manipulate queries, alter database records, and even bypass authentication (if login is implemented insecurely).
- Lacks proper validation and uses raw string-based SQL queries.

---

## 🧰 Technologies Used

| Technology | Purpose                                |
|------------|----------------------------------------|
| Python 3.x | Core programming language              |
| Flask      | Web framework used to build the app    |
| SQLite3    | Lightweight relational database        |
| HTML       | Used for building the frontend (forms) |

---

📁 Project Structure

```plaintext
│
├── vulnerable_voting_app/
│   ├── app.py               # Main Flask application with vulnerabilities
│   ├── init_db.py           # Initializes database with tables and sample data
│   ├── templates/           # HTML templates
│   │   ├── vote.html
│   │   └── results.html
│   └── vulnerable_voting_app.jpg  # Architecture diagram (if any)
│
└── README.md                # Project documentation

---

⚙️ Setup Instructions
Requirements: Python 3.x

Clone the repository:


git clone https://github.com/yourusername/voting-app.git
cd voting-app
Install Flask if not already installed:


pip install flask
Initialize the database:

python init_db.py
Run the application:


python app.py
Open your browser and visit:


http://127.0.0.1:5000

---

SQL Injection Demonstration
📝 Vote Form Injection
Try submitting this as input for the Candidate ID field in the vote form:


1'), 1); UPDATE votes SET vote_count = 999 WHERE candidate_id = '1'; --
🔐 Result Bypass Injection
Try submitting this input to bypass login:


' OR '1'='1
🧱 What's Vulnerable?
SQL queries built using string concatenation or f-strings.

No use of parameterized queries.

Lack of input sanitization and validation.

Use of executescript() that allows stacked SQL queries.

No use of secure authentication mechanisms (in insecure login scenarios).

🔒 Security Risks Explained
The app demonstrates how improper coding practices can lead to:

✅ Data tampering (e.g., modifying vote counts)
✅ Data leakage (e.g., exposing votes, users)
✅ Authentication bypass (e.g., logging in with ' OR '1'='1)

🔮 Future Improvements
🔐 Implement secure user authentication and session management with hashed passwords (e.g., using bcrypt).

👥 Add role-based access control (RBAC) to restrict admin operations.

🧼 Use security libraries to sanitize inputs.
