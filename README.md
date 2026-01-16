## 📦 Inventory & Reorder Algorithm API
# 🚀 Project Overview

This project is a RESTful Inventory Management API built using FastAPI and PostgreSQL.
It allows managing products in an inventory and automatically identifies products that need to be reordered based on a simple business rule.

## 🛠️ Tech Stack
- Backend Framework: FastAPI
- ASGI Server: Uvicorn
- Database: PostgreSQL
- ORM: SQLAlchemy
- Data Validation: Pydantic
- API Documentation: Swagger UI (auto-generated)

## 📁 Project Structure (Current)
```
 inventory/
      ├── main.py
      ├── models/
      │   ├── database.py
      │   └── model.py
      ├── schemas/
      │   └── product.py
      |__ requirements.txt
      ├── README.md
```

# ⚙️ Environment Setup

## 1️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

# 2️⃣ Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
(or from requirements.txt if created)

## 🗄️ Database Setup (PostgreSQL)
1.Open pgAdmin
2.Create a database (example):
 inventory_db
3.Update database connection in models/database.py

 DATABASE_URL = "postgresql://username:password@localhost:5432/inventory_db"

 Tables are created automatically using:
    Base.metadata.create_all(bind=engine)

## 📌 API Endpoints
🔹 Create Product
    POST /products

* Request Body (JSON):
{
  "name": "Pen",
  "current_stock": 50,
  "min_reorder_level": 20,
  "price": 10.5
}
🔹 Get All Products:
    GET /products

🔹 Update Product:
    PUT /products/{product_id}

🔹 Delete Product:
    DELETE /products/{product_id}

🔹 Reorder Recommendation:
    GET /inventory/reorder_recommendations

# Reorder Logic:
- A product is recommended for reorder if:
- current_stock <= 1.25 × min_reorder_level

# 📖 API Documentation

- Once the server is running, open:
- Swagger UI:
- http://127.0.0.1:8000/docs

# ▶️ Running the Application
- uvicorn inventory.main:app --reload
