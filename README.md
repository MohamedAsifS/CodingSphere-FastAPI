# CodingSphere-FastAPI

# ⚡ CodingSphere Auth API - FastAPI + JWT + RBAC

This project implements a secure authentication API using **FastAPI**, **JWT**, and **Role-Based Access Control (RBAC)**. It allows user registration, login, and role-based access control to endpoints.

🔗 **Live Swagger Documentation**: [https://codingsphere-fastapi-1.onrender.com/docs](https://codingsphere-fastapi-1.onrender.com/docs)

---

## 🌐 Hosted On

**Render**: FastAPI app hosted with SQLite  
[View Live API Docs](https://codingsphere-fastapi-1.onrender.com/docs)

---

## 🛠️ Local Setup

### Prerequisites

- Python 3.8+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/codingsphere-auth-api.git
cd codingsphere-auth-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Activate it
venv\Scripts\activate        # On Windows
source venv/bin/activate       # On Linux/macOS
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

⚙️ Configuration

Create or modify the existing .env file in the root directory:

DATABASE_URL=sqlite:///./demo.db
SECRET_KEY=<your_secret_key_from_jwtsecret.com>

To generate a strong secret key, visit:🔐 https://jwtsecret.com/generate

Generate a secure key here: [jwtsecret.com](https://jwtsecret.com/generate)

---

## 🚀 Run the Application

```bash
uvicorn app.main:app --reload
```

The app will run at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing the API

You can test the API using:

- 🔸 **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 🔸 **Postman**: Import your routes and test authenticated/unauthenticated access

---

## 📹 Demo Video

▶️ [Watch Setup & Usage](https://www.youtube.com/watch?v=your_video_id)  
*(Replace with your demo link)*

---

## 📁 .gitignore

Make sure your repository includes the following in `.gitignore`:

```gitignore
__pycache__/
*.py[cod]
.env
venv/
*.db
```

---

## 📌 Project Structure

```
app/
│
├── main.py               # FastAPI application entrypoint
├── models/               # SQLAlchemy models
├── schemas/              # Pydantic schemas
├── router/               # API endpoints
├── repository/           # Logic for DB operations
└── database/             # DB connection and config
```

---

## ✅ Submit Assignment

When you're ready, submit your GitHub repo at:  
📨 [Assignment Submission Form](https://forms.gle/PsffvY3dyJCZpL5z5)

---

## 📃 License

This project is licensed for educational and assessment use.
