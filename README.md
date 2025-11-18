# Microservices: User Service & Auth Service

This project demonstrates a simple microservice architecture using **FastAPI**, applying clean code practices and the **SOLID (S & D)** principles.  
The system consists of two independent services:

- **User Service (port 8001)** – manages user data  
- **Auth Service (port 8002)** – handles registration and login

Both services communicate via HTTP requests.

---

## 🚀 Running the Services

Run both services from the project root:
uvicorn service_user.app:app --reload --port 8001 & uvicorn service_auth.app:app --reload --port 8002

Or run separately:
uvicorn service_user.app:app --reload --port 8001
uvicorn service_auth.app:app --reload --port 8002

📌 API Documentation
User Service Swagger: http://127.0.0.1:8001/docs

Auth Service Swagger: http://127.0.0.1:8002/docs

🔧 Installation

pip install -r requirements.txt
pip install "pydantic[email]"
pip install email-validator

📂 Project Structure

service_user/
service_auth/
common/
README.md

Each service includes:

- [ ] controller.py – API endpoints

- [ ] interfaces.py – abstract service contracts

- [ ] service_impl.py – business logic implementation

- [ ] dependencies.py – DI bindings

schemas.py – request/response models

✨ Features
- [ ] Clean separation between business logic and controllers

- [ ] Dependency injection using abstractions

- [ ] Email validation

- [ ] Simple registration and login flow

- [ ] Two fully isolated FastAPI microservices



👤 Author
Aizhan
