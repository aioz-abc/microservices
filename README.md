# Microservices: User Service & Auth Service

Two independent **FastAPI** services that talk to each other over HTTP, built to practise clean
architecture: business logic hidden behind interfaces, wired in through dependency injection
(the **S** and **D** of SOLID).

| Service | Port | Responsibility |
|---|---|---|
| **User Service** | 8001 | stores users, looks them up by email |
| **Auth Service** | 8002 | registration and login; calls the User Service over HTTP |

## Architecture

```
client ──▶ Auth Service (8002) ──HTTP──▶ User Service (8001)
            controller.py                 controller.py
               │ depends on                  │ depends on
            interfaces.py (abstract)      interfaces.py (abstract)
               │ implemented by              │ implemented by
            service_impl.py               service_impl.py
```

Each service has the same layers:

- `controller.py`: API endpoints only, no business logic
- `interfaces.py`: abstract service contract
- `service_impl.py`: the implementation
- `dependencies.py`: binds the interface to the implementation (DI)

Shared request/response models live in `common/schemas.py`. Emails are validated by Pydantic.

## Run

```bash
pip install -r requirements.txt "pydantic[email]"

uvicorn service_user.app:app --reload --port 8001
uvicorn service_auth.app:app --reload --port 8002
```

Swagger docs: http://127.0.0.1:8001/docs and http://127.0.0.1:8002/docs

## Scope

This is a learning project about service boundaries and DI. Users are kept in memory and the auth
token is a placeholder, so it's not meant for production.

## Tech stack

Python · FastAPI · Pydantic · Uvicorn · requests
