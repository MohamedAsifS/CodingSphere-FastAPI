# CodingSphere-FastAPI
# CodingSphere-FastAPI

# ⚡ CodingSphere Auth API - FastAPI + JWT + RBAC

This project implements a secure authentication API using **FastAPI**, **JWT**, and **Role-Based Access Control (RBAC)**. It allows user registration, login, and role-based access control to endpoints.

🔗 **Live Swagger Documentation**: [https://codingsphere-fastapi-1.onrender.com/docs](https://codingsphere-fastapi-1.onrender.com/docs)

---

## 🌐 Hosted On

**Render**: FastAPI app hosted with SQLite  
[View Live API Docs](https://codingsphere-fastapi-1.onrender.com/docs)

---

## 📌 Project Structure

```
project-root/
│
├── app/
│ ├── main.py # FastAPI application entrypoint
│ ├── models/ # SQLAlchemy models
│ ├── schemas/ # Pydantic schemas
│ ├── router/ # API endpoints
│ ├── repository/ # Logic for DB operations
│ ├── database/ # DB connection and config
│ └── auth/ # JWT handling, password hashing, and role-based authentication
│
├── .env # Environment variables (e.g., DB URI, JWT secret)
│ # ➤ Example:
│ # DATABASE_URL=sqlite:///./demo.db
│ # SECURITY_KEY=your_generated_key
│
├── requirements.txt # Python dependencies
│ # ➤ Install with:
│ # pip install -r requirements.txt
│
├── .gitignore # Files/directories to exclude from Git
│
└── README.md # Project documentation
```

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

### 4. Configure `.env`

A .env file already exists in the root folder. Update it with:

```env
DATABASE_URL=sqlite:///../demo.db
SECURITY_KEY=your_generated_secret_key
```

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



# Thank You! 🙏

Thank you for checking out this project! I appreciate your time and interest.

If you have any questions, feedback, or suggestions, feel free to reach out to me:

📧 **Email**: [maasifar@gmail.com](mailto:maasifar@gmail.com)  
📱 **Phone**: +91 8668141852

Your support means a lot! 😊

---

> _"Innovation is the key to progress."_ 🚀


