# 🍔 Food Delivery Backend (Python)

A production-style **Food Delivery Backend** built in Python to learn backend engineering from the ground up.

Instead of building a simple CRUD application, this project follows a real software engineering workflow, including:

- Requirements Analysis
- UML Design
- Object-Oriented Programming (OOP)
- SOLID Principles
- Design Patterns
- Layered Architecture
- Repository Pattern
- FastAPI (Upcoming)
- PostgreSQL (Upcoming)

The project is being developed **sprint by sprint**, similar to how real software teams build production systems.

---

## 🎯 Project Goal

The goal of this project is to understand **how real backend applications are designed**, not just how to write Python code.

Each sprint focuses on learning and applying software engineering concepts before moving to implementation.

---

## 📂 Current Project Structure

```
food-delivery-backend-python/
│
├── Documents/
│   └── uml.excalidraw
│
├── data/
│   └── Restaurants_Repository.json
│
├── models/
│   ├── owner.py
│   ├── restaurant.py
│   ├── category.py
│   └── menu_item.py
│
├── repositories/
│   └── restaurant_repository.py
│
├── main.py
└── README.md
```

---

## ✅ Completed Sprints

### Sprint 1 — Requirements & System Design

- Business Requirements
- Domain Analysis
- Business Rules
- UML Class Diagram
- Entity Relationships
- Object-Oriented Design

---

### Sprint 2 — Domain Models

Implemented core domain models:

- ✅ Owner
- ✅ Restaurant
- ✅ Category
- ✅ MenuItem

Concepts practiced:

- Classes & Objects
- Encapsulation
- Composition
- Association
- Business Methods
- Clean Class Design

---

## Sprint 3 — Repository Pattern

Implemented a persistence layer using the Repository Pattern.

### Repository Features

- ✅ Create JSON storage
- ✅ Save entities
- ✅ Retrieve all entities
- ✅ Find entity by ID
- ✅ Update entity
- ✅ Delete entity

### Serialization

Implemented serialization for all domain models using:

- `to_dict()`
- `from_dict()`

### Concepts Practiced

- Repository Pattern
- Separation of Concerns
- Data Persistence
- JSON Serialization
- Layered Architecture
- Single Responsibility Principle


---

## 🚀 Upcoming Sprints

- Repository Pattern
- Service Layer
- Dependency Injection
- Authentication
- Authorization
- Customer Module
- Cart System
- Order Management
- Payment Integration
- Delivery Management
- Notifications
- PostgreSQL
- FastAPI REST APIs
- Unit Testing
- Deployment

---

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming
- UML
- Git & GitHub

**Upcoming**

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication

---

## 📖 Learning Objectives

This project is designed to strengthen knowledge of:

- Python OOP
- SOLID Principles
- Software Design
- UML
- Design Patterns
- Clean Architecture
- Backend Development
- REST API Development

---

## 📌 Development Approach

Each feature is implemented following this workflow:

```
Requirements
      ↓
Business Rules
      ↓
UML Design
      ↓
Domain Model
      ↓
Implementation
      ↓
Testing
      ↓
Refactoring
```

---


# 📈 Project Status

**Current Version**

**v1.1.0**

**Current Sprint**

✅ Sprint 3 — Repository Pattern

**Next Sprint**

🚀 Sprint 4 — Service Layer

---

## 🤝 Feedback

I'm building this project as part of my backend development journey. Feedback, suggestions, and code reviews are always welcome.

If you find something that can be improved, feel free to open an issue or submit a pull request.

---

## 👨‍💻 Author

**Mian Rahaib**

- Python Backend Developer (Learning Journey)
- BS Mathematics & Data Science
- Building production-style backend projects with Python