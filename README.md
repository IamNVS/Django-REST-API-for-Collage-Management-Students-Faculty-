# Django-REST-API-for-Collage-Management-Students-Faculty-
A Django REST Framework-based API for managing collages, students, and faculty. Each collage can have multiple students and faculty. Supports searching for students and faculty by ID within a collage. Only admin users can add, update, and delete records. Uses SQLite as the database.

# Django REST API for Collage Management (Students & Faculty)

## 📌 Overview
This is a **Django REST Framework (DRF)** project for managing collages, students, and faculty members.  
Each **Collage** can have multiple **Students** and **Faculty**.  
- Allows searching for **Students** and **Faculty** by ID within a specific collage.
- **Only Admin Users** can perform **add, update, and delete** operations.
- Uses **SQLite** as the database.

---

## 🚀 Features
✅ **CRUD Operations** for Collage, Student, and Faculty  
✅ **One-to-Many Relationship:** A collage can have multiple students and faculty  
✅ **Search Functionality:** Find students and faculty in a collage by ID  
✅ **Admin-Only Access:** Only admins can modify data  
✅ **Django Admin Panel** for managing records  
✅ **SQLite Database** for lightweight data storage  

---

## 📦 Tech Stack
- **Django** (Python Web Framework)
- **Django REST Framework (DRF)** (For building APIs)
- **SQLite** (Default lightweight database)
- **JWT Authentication** (For admin access control)

---

## 🛠 Installation & Setup

## 🛠 Installation & Setup

Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/collage-management-api.git
cd collage-management-api
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations & Create Superuser
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 5️⃣ Run the Development Server
```sh
python manage.py runserver
```
The API will be available at:  
📌 **`http://127.0.0.1:8000/api/v1/`**

---

## 📌 API Endpoints

### **Collage API**
| Method | Endpoint | Description | Access |
|--------|---------|-------------|---------|
| **GET** | `/api/v1/collages/` | List all collages | Open |
| **POST** | `/api/v1/collages/` | Create a new collage | Admin Only |
| **GET** | `/api/v1/collages/{id}/` | Retrieve a specific collage | Open |
| **PUT** | `/api/v1/collages/{id}/` | Update a collage | Admin Only |
| **DELETE** | `/api/v1/collages/{id}/` | Delete a collage | Admin Only |

### **Student API**
| Method | Endpoint | Description | Access |
|--------|---------|-------------|---------|
| **GET** | `/api/v1/collages/{id}/students/` | List students in a collage | Open |
| **POST** | `/api/v1/students/` | Add a new student | Admin Only |

### **Faculty API**
| Method | Endpoint | Description | Access |
|--------|---------|-------------|---------|
| **GET** | `/api/v1/collages/{id}/faculty/` | List faculty in a collage | Open |
| **POST** | `/api/v1/faculty/` | Add a new faculty member | Admin Only |

---

## 🔐 Authentication & Permissions
- **Admin Authentication:** Uses Django Admin for managing users.
- **Permissions:** Only **admin users** can create, update, or delete records.
- **Public Access:** Anyone can view collages, students, and faculty.

---

## 🔍 Search Functionality
You can search for a **Student or Faculty** in a **Collage** using their ID:

### 🔹 Search for a Student in a Collage
```http
GET /api/v1/collages/{collage_id}/students/{student_id}/
```

### 🔹 Search for a Faculty Member in a Collage
```http
GET /api/v1/collages/{collage_id}/faculty/{faculty_id}/
```

---
