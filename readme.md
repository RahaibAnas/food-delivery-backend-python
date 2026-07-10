# 🍔 Food Delivery Backend (Python)

A production-style **Food Delivery Backend** built in Python, developed sprint by sprint to simulate real-world backend engineering practices. The project applies OOP, SOLID principles, layered architecture, authentication, authorization, and design patterns before evolving into a FastAPI and PostgreSQL-based production backend.

Instead of building a simple CRUD application, this project follows a real software engineering workflow, including:

- Requirements Analysis
- UML Design
- Object-Oriented Programming (OOP)
- SOLID Principles
- Design Patterns
- Layered Architecture
- Repository Pattern
- Service Layer
- Controller Layer
- Dependency Injection
- FastAPI (Upcoming)
- PostgreSQL (Upcoming)

The project is being developed **sprint by sprint**, similar to how real software teams build production systems.

---

# 🎯 Project Goal

The goal of this project is to understand **how real backend applications are designed**, not just how to write Python code.

Each sprint focuses on learning and applying software engineering concepts before moving to implementation.

---

# 📂 Current Project Structure

```
food-delivery-backend-python/

│
├── Documents/
│
├── application/
│   └── app.py
│
├── controllers/
│   ├── auth_controller.py
│   └── restaurant_controller.py
│
├── services/
│   ├── auth_service.py
│   └── restaurant_service.py
│
├── repositories/
│   ├── owner_repository.py
│   └── restaurant_repository.py
│
├── exceptions/
│   ├── auth_exceptions.py
│   ├── authorization_exceptions.py
│   ├── restaurant_exceptions.py
│   └── validation_exceptions.py
│
├── models/
│   ├── owner.py
│   ├── restaurant.py
│   ├── category.py
│   └── menu_item.py
│
├── data/
│   ├── Owners_Repository.json
│   └── Restaurants_Repository.json
│
├── main.py
├── README.md
└── CHANGELOG.md
```
---

# ✅ Completed Sprints

## Sprint 1 — Requirements & System Design

### Completed

- ✅ Business Requirements
- ✅ Domain Analysis
- ✅ Business Rules
- ✅ UML Class Diagram
- ✅ Entity Relationships
- ✅ Object-Oriented Design

### Concepts Practiced

- Requirement Analysis
- Domain Modeling
- UML
- Software Design

---

## Sprint 2 — Domain Models

Implemented core domain models.

### Models

- ✅ Owner
- ✅ Restaurant
- ✅ Category
- ✅ MenuItem

### Concepts Practiced

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

- ✅ Create JSON Storage
- ✅ Save Entities
- ✅ Retrieve All Entities
- ✅ Find Entity by ID
- ✅ Update Entity
- ✅ Delete Entity

### Serialization

Implemented serialization for all domain models using:

- `to_dict()`
- `from_dict()`

### Concepts Practiced

- Repository Pattern
- Separation of Concerns
- JSON Persistence
- Object Serialization
- Layered Architecture
- Single Responsibility Principle

---

## Sprint 4 — Service Layer

Implemented the application's business logic using a dedicated **Service Layer**.

The service layer acts as the bridge between the application and the repository, ensuring that all business rules are validated before data is persisted.

### Restaurant Management

- ✅ Create Restaurant
- ✅ Get Restaurant by ID
- ✅ Get All Restaurants
- ✅ Update Restaurant
- ✅ Delete Restaurant
- ✅ Open Restaurant
- ✅ Close Restaurant

### Category Management

- ✅ Add Category
- ✅ Remove Category

### Menu Management

- ✅ Add Menu Item
- ✅ Remove Menu Item

### Business Validations

- ✅ Restaurant Validation
- ✅ Restaurant Duplicate Detection
- ✅ Opening & Closing Time Validation
- ✅ Category Validation
- ✅ Duplicate Category Detection
- ✅ Menu Item Validation
- ✅ Duplicate Menu Item Detection

### Concepts Practiced

- Service Layer Pattern
- Business Logic Separation
- Layered Architecture
- Dependency Injection
- Domain Validation
- Exception Handling
- Clean Code
- Single Responsibility Principle

---

## Sprint 5 — Controller Layer

Implemented a dedicated **Controller Layer** that acts as the application's entry point.

The controller receives requests, delegates them to the service layer, handles exceptions, and returns responses without containing business logic.

### Restaurant Controller

- ✅ Create Restaurant
- ✅ Get Restaurant by ID
- ✅ Get All Restaurants
- ✅ Update Restaurant
- ✅ Delete Restaurant
- ✅ Open Restaurant
- ✅ Close Restaurant

### Category Controller

- ✅ Add Category
- ✅ Remove Category

### Menu Controller

- ✅ Add Menu Item
- ✅ Remove Menu Item

### Concepts Practiced

- Controller Layer Pattern
- Separation of Concerns
- Dependency Injection
- Exception Handling
- Layered Architecture
- Thin Controllers
- Clean Architecture

---

## Sprint 6 — Application Layer

Implemented an Application Layer that serves as the application's composition root.

The application layer is responsible for creating and connecting repositories, services, and controllers using dependency injection.

### Features

- ✅ FoodDeliveryApp
- ✅ Application Startup
- ✅ Dependency Injection
- ✅ Composition Root
- ✅ Controller Registration
- ✅ Service Registration
- ✅ Repository Registration

### Concepts Practiced

- Application Layer
- Composition Root
- Dependency Injection
- Object Composition
- Layered Architecture
- Clean Architecture

---

## Sprint 7 — Authentication & Authorization

Implemented a complete authentication and authorization system for restaurant owners.

### Authentication

- ✅ Owner Registration
- ✅ Owner Login
- ✅ Owner Logout
- ✅ Session Management
- ✅ Password Verification
- ✅ Password Change
- ✅ Duplicate Email Detection

### Authorization

- ✅ Login Required for Protected Operations
- ✅ Restaurant Ownership Verification
- ✅ Protected Restaurant Updates
- ✅ Protected Restaurant Deletion
- ✅ Protected Category Management
- ✅ Protected Menu Management

### Authentication Enhancements

- ✅ Custom Exception Hierarchy
- ✅ Improved Error Handling
- ✅ Domain-Specific Exceptions

### Concepts Practiced

- Authentication
- Authorization
- Session Management
- Access Control
- Dependency Injection
- Custom Exceptions
- Exception Hierarchy
- Controller Exception Handling
- Service Layer Security

---

# 🚀 Upcoming Sprints

- Authentication & Authorization
- Customer Module
- Cart System
- Order Management
- Payment Integration
- Delivery Management
- Notifications
- FastAPI REST APIs
- PostgreSQL Integration
- SQLAlchemy ORM
- Unit Testing
- Logging
- Docker
- Deployment

---

# 🛠️ Technologies

## Current

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- UML
- Git
- GitHub

## Upcoming

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Docker

---

# 📖 Learning Objectives

This project is designed to strengthen knowledge of:

- Python OOP
- SOLID Principles
- Software Design
- UML Modeling
- Design Patterns
- Repository Pattern
- Service Layer
- Controller Layer
- Application Layer
- Composition Root
- Dependency Injection
- Layered Architecture
- Clean Architecture
- Authentication
- Authorization
- Access Control
- Custom Exceptions
- Exception Handling
- Backend Development
- REST API Development

---

# 🏗️ Architecture

```
                Client
                   │
                   ▼
            FoodDeliveryApp
              │         │
              ▼         ▼
   AuthController   RestaurantController
          │                 │
          ▼                 ▼
    AuthService      RestaurantService
          │                 │
          ▼                 ▼
 OwnerRepository   RestaurantRepository
          │                 │
          └──────────┬──────┘
                     ▼
                JSON Database
```

Each layer has a single responsibility.

- **Controller** → Handles requests and exceptions.
- **Service** → Contains business rules and validations.
- **Repository** → Handles data persistence.
- **Models** → Represent business entities.

---

# 📌 Development Workflow

Every feature follows the same software engineering workflow.

```
Requirements
      │
      ▼
Business Rules
      │
      ▼
UML Design
      │
      ▼
Domain Models
      │
      ▼
Repository Layer
      │
      ▼
Service Layer
      │
      ▼
Controller Layer
      │
      ▼
Application layer
      |
      ▼
Testing
      │
      ▼
Refactoring
```

---

# 📈 Project Status

## Current Version

**v1.5.0**

## Current Sprint

✅ Sprint 7 — Authentication & Authorization

## Next Sprint

🚀 Sprint 8 — Customer Module

---

# 🗺️ Roadmap

- [x] Sprint 1 — Requirements & UML
- [x] Sprint 2 — Domain Models
- [x] Sprint 3 — Repository Layer
- [x] Sprint 4 — Service Layer
- [x] Sprint 5 — Controller Layer
- [x] Sprint 6 — Application Layer
- [x] Sprint 7 — Authentication & Authorization
- [ ] Sprint 8 — Customer Module
- [ ] Sprint 9 — Cart Module
- [ ] Sprint 10 — Order Management
- [ ] Sprint 11 — Payment Integration
- [ ] Sprint 12 — Delivery Management
- [ ] Sprint 13 — FastAPI REST APIs
- [ ] Sprint 14 — PostgreSQL & SQLAlchemy
- [ ] Sprint 15 — Unit Testing & Logging
- [ ] Sprint 16 — Docker & Deployment

---

# 🎯 Project Vision

This project is being developed incrementally to simulate a production-grade backend system.

By the end of development, the project will include:

### Completed

- Restaurant Management
- Menu Management
- Owner Authentication
- Authorization
- Layered Architecture
- Repository Pattern
- Service Layer
- Controller Layer
- Application Layer

### Planned

- Customer Management
- Shopping Cart
- Order Processing
- Payment Gateway Integration
- Delivery Tracking
- REST APIs using FastAPI
- PostgreSQL Database
- SQLAlchemy ORM
- JWT Authentication
- Unit Testing
- Docker Deployment

---

# 🤝 Feedback

I'm building this project as part of my backend development journey.

Feedback, suggestions, and code reviews are always welcome.

If you find something that can be improved, feel free to open an issue or submit a pull request.

---

# 👨‍💻 Author

**Mian Rahaib**

- BS Mathematics & Data Science
- Aspiring Python Backend Developer
- Learning Software Engineering through Production-Style Projects

---

⭐ If you found this project helpful or interesting, consider giving it a star!