# 🪙 Crypto Market Alert & Portfolio Tracker Backend

A backend service built with **FastAPI** that tracks crypto prices, allows users to set price alerts, and manage a virtual portfolio.  
This project demonstrates real-time event handling, async tasks, and clean architecture for trading systems.

---

##  Features

- Fetch simulated live crypto prices
- Create and manage user-defined price alerts
- Manage a crypto portfolio
- RESTful API with FastAPI
- SQLite database (can switch to PostgreSQL/MySQL easily)
- Async background updates for live prices

---

## Project Structure
crypto_market_backend/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI entry point
│ ├── database.py # Database connection
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # CRUD logic for DB
│ ├── auth.py # (optional) Authentication handlers
│
├── requirements.txt # Dependencies
├── .gitignore
└── README.md # Project documentation



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/srivastavav427-code/crypto_market_backend.git
cd crypto_market_backend


