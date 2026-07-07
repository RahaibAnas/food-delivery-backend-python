# Changelog

All notable changes to this project will be documented in this file.

This project follows a sprint-based development approach inspired by real-world software engineering practices.

The format is based on **Keep a Changelog**, and versioning loosely follows **Semantic Versioning**.

---

## [v1.2.0] - 2026-07-07

### Added

#### Service Layer

- Added `RestaurantService`
- Introduced business logic layer between models and repositories
- Applied Dependency Injection using `RestaurantRepository`

#### Restaurant Management

- Create Restaurant
- Get Restaurant by ID
- Get All Restaurants
- Update Restaurant
- Delete Restaurant
- Open Restaurant
- Close Restaurant

#### Category Management

- Add Category
- Remove Category

#### Menu Management

- Add Menu Item
- Remove Menu Item

#### Business Validations

- Restaurant validation
- Category validation
- Menu item validation
- Opening & closing time validation
- Duplicate restaurant detection
- Duplicate category detection
- Duplicate menu item detection

#### Internal Helper Methods

- Find category inside restaurant
- Find menu item inside category

### Improved

- Better separation of concerns
- Business logic moved out of repositories
- Cleaner layered architecture
- Improved exception handling
- Reduced code duplication

---

## [v1.1.0] - 2026-07-06

### Added

#### Repository Pattern

- Generic JSON persistence
- Create repository file
- Read all entities
- Write all entities
- Save entity
- Find entity by ID
- Update entity
- Delete entity

#### Serialization

Implemented serialization for all domain models using:

- `to_dict()`
- `from_dict()`

### Improved

- Separated persistence from domain models
- Added data layer
- Improved project architecture

---

## [v1.0.0] - 2026-07-05

### Initial Release

#### Project Initialization

- Created project structure
- Added UML design
- Defined business requirements
- Created domain model

#### Domain Models

- Owner
- Restaurant
- Category
- MenuItem

#### Concepts Practiced

- Object-Oriented Programming
- Encapsulation
- Composition
- Association
- UML Modeling
- Business Methods

---

## Upcoming

- Controller Layer
- Authentication
- Authorization
- Customer Module
- Cart System
- Order Management
- Payment Integration
- Delivery Management
- Notifications
- FastAPI
- PostgreSQL
- SQLAlchemy
- Unit Testing
- Docker
- Deployment