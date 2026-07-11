# Changelog

All notable changes to this project will be documented in this file.

This project follows a sprint-based development approach inspired by real-world software engineering practices.

The format is based on **Keep a Changelog**, and versioning loosely follows **Semantic Versioning**.

---

## [v1.6.0] - 2026-07-11

### Added

#### Customer Module

- Added `Customer` domain model
- Added `CustomerRepository`
- Added `CustomerService`
- Added `CustomerController`

#### Customer Authentication

- Customer Registration
- Customer Login
- Customer Logout
- Session Management
- Password Change

#### Customer Management

- Get Customer by ID
- Get All Customers
- Update Customer Profile
- Delete Customer Account

#### Business Validation

- Customer validation
- Duplicate email detection
- Duplicate phone number detection
- Password validation
- Authentication checks


### Improved

- Added customer workflow alongside owner workflow
- Reused layered architecture across multiple modules
- Improved code reusability

---

## [v1.5.0] - 2026-07-10

### Added

#### Authentication Module

- Added `OwnerRepository`
- Added `AuthService`
- Added `AuthController`
- Implemented owner registration
- Implemented owner login
- Implemented owner logout
- Added in-memory session management using `current_user`

#### Authorization

- Added login-required authorization checks
- Restricted restaurant management to authenticated owners
- Restricted restaurant updates to the restaurant owner
- Restricted restaurant deletion to the restaurant owner
- Restricted restaurant open/close operations to the restaurant owner
- Restricted category management to the restaurant owner
- Restricted menu management to the restaurant owner

#### Owner Features

- Added password support
- Added password verification
- Added password change functionality

#### Exception Handling

- Introduced custom exception hierarchy
- Replaced generic exceptions with domain-specific exceptions
- Improved controller-level exception handling
- Improved service-layer error reporting

### Improved

- Strengthened separation between authentication and restaurant modules
- Improved security by enforcing ownership rules
- Reduced unauthorized access to business operations
- Improved maintainability through custom exceptions
- Better service and controller architecture

---

## [v1.4.0] - 2026-07-08

### Added

#### Application Layer

- Added `FoodDeliveryApp`
- Introduced Application Layer as the composition root
- Centralized dependency initialization
- Connected Repository → Service → Controller
- Added dependency injection at application startup

### Improved

- Removed object creation responsibilities from `main.py`
- Simplified application startup
- Improved scalability for future modules
- Better dependency management
- Cleaner project architecture

---

## [v1.3.0] - 2026-07-08

### Added

#### Controller Layer

- Added `RestaurantController`
- Introduced Controller Layer above the Service Layer
- Applied Dependency Injection using `RestaurantService`

#### Restaurant Controller

- Create Restaurant
- Get Restaurant by ID
- Get All Restaurants
- Update Restaurant
- Delete Restaurant
- Open Restaurant
- Close Restaurant

#### Category Controller

- Add Category
- Remove Category

#### Menu Controller

- Add Menu Item
- Remove Menu Item

### Improved

- Added application entry layer
- Better separation between presentation and business logic
- Centralized exception handling
- Reduced responsibilities of `main.py`
- Improved layered architecture

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