# 🔐 OTP Authentication System (Django + React)

A full-stack **OTP-based authentication system** built using **Django REST Framework and React**.
This project demonstrates secure user authentication using **One-Time Password (OTP) verification via email**.

---

# 🚀 Features

* User Registration
* User Login with Username & Password
* Email-based OTP verification
* OTP expiration system (5 minutes)
* Resend OTP functionality
* OTP countdown timer
* Error handling and validation messages
* Beautiful UI with Tailwind CSS
* Secure backend using Django REST API

---

# 🛠 Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* SMTP Email (Gmail)
* SQLite Database

### Frontend

* React.js
* Axios
* Tailwind CSS

---

# 📂 Project Structure

```
otp-auth-system
│
├── backend
│   ├── otp_project
│   │   ├── accounts
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── serializers.py
│   │   │   └── urls.py
│   │   │
│   │   ├── otp_project
│   │   │   ├── settings.py
│   │   │   └── urls.py
│   │   │
│   │   └── manage.py
│   │
│   └── venv
│
└── frontend
    ├── src
    │   └── App.js
    └── package.json
```

---

# ⚙️ Backend Setup (Django)

### 1️⃣ Navigate to backend

```
cd backend
```

### 2️⃣ Activate virtual environment

Windows

```
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install django djangorestframework corsheaders
```

### 4️⃣ Run migrations

```
python manage.py migrate
```

### 5️⃣ Start Django server

```
python manage.py runserver
```

Backend will run on:

```
http://127.0.0.1:8000
```

---

# ⚙️ Frontend Setup (React)

### 1️⃣ Navigate to frontend

```
cd frontend
```

### 2️⃣ Install dependencies

```
npm install
```

### 3️⃣ Start React app

```
npm start
```

Frontend will run on:

```
http://localhost:3000
```

---

# 🔄 Authentication Flow

```
Register User
     ↓
Login with Username & Password
     ↓
Server generates OTP
     ↓
OTP sent via Email
     ↓
User enters OTP
     ↓
Server verifies OTP
     ↓
Login Successful
```

---

# 🔑 API Endpoints

### Register

```
POST /api/register/
```

Example request:

```
{
  "username": "user1",
  "email": "user@example.com",
  "password": "SecurePass123"
}
```

---

### Login

```
POST /api/login/
```

Example request:

```
{
  "username": "user1",
  "password": "SecurePass123"
}
```

---

### Verify OTP

```
POST /api/verify-otp/
```

Example request:

```
{
  "username": "user1",
  "otp": "123456"
}
```

---

# ⏱ OTP Security

* OTP expires after **5 minutes**
* New OTP generated for every login
* OTP delivered via **SMTP email**

---

# 🎨 UI Features

* Responsive design
* Tailwind CSS styling
* OTP countdown timer
* Resend OTP button
* Clear validation messages

---

# 📸 Future Improvements

* JWT Authentication
* Password reset via OTP
* User profile dashboard
* Deployment on cloud (Render / Vercel)
* Rate limiting for OTP requests

---

# 👨‍💻 Author

**Piyush Vinde**

B.Tech Computer Engineering
Aspiring DevOps Engineer / Developer

---

# ⭐ If you like this project

Give it a **star ⭐ on GitHub** and feel free to contribute.
