# AP Auth Service

Authentication microservice for **AP Self Storage**, a self-hosted personal cloud storage platform.

This service is responsible for handling user authentication and will eventually provide secure authentication mechanisms for the other services within the platform.

> **Project status:** Early development. The FastAPI application and initial authentication endpoint are implemented. Database integration and actual credential verification are not yet implemented.

## Current Features

- FastAPI application initialization.
- Modular API architecture using `APIRouter`.
- Pydantic request validation.
- Initial `POST /auth/login` endpoint.
- Email format validation using `EmailStr`.
- Interactive API documentation through Swagger UI.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| FastAPI | API framework |
| Uvicorn | ASGI server |
| Pydantic | Request validation |
| Email Validator | Email format validation |

Additional dependencies are declared in `requirements.txt` for upcoming development.

## Project Structure

```text
ap-auth-service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── route_auth.py
│   └── structure/
│       ├── __init__.py
│       └── auth.py
├── tests/
│   └── __init__.py
├── requirements.txt
└── .gitignore
```

### Application Modules

- **main.py:** Initializes the FastAPI application and registers API routers.
- **routers/:** Contains API endpoints grouped by functionality.
- **structure/:** Contains Pydantic models defining request and response structures.
- **tests/:** Reserved for automated tests.

## Current API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/login` | Initial login endpoint |

**Example request:**

```http
POST /auth/login
Content-Type: application/json
```

```json
{
  "email": "user@example.com",
  "password": "examplepassword"
}
```

**Current response:**

```json
{
  "message": "ok"
}
```

At this stage, the endpoint validates the request structure and email format. It does not yet authenticate users or verify passwords.

## Roadmap

- [x] Initialize FastAPI application.
- [x] Establish modular project structure.
- [x] Implement authentication router.
- [x] Implement login request schema.
- [x] Register authentication router in the main application.
- [x] Test initial endpoint using cURL.
- [x] Document project dependencies.
- [ ] Set up PostgreSQL.
- [ ] Implement SQLAlchemy database integration.
- [ ] Create user database model.
- [ ] Configure Alembic migrations.
- [ ] Implement Argon2id password hashing and verification.
- [ ] Implement local administrator account creation.
- [ ] Implement actual login credential verification.
- [ ] Implement JWT access tokens.
- [ ] Implement refresh token rotation and revocation.
- [ ] Add automated tests.
- [ ] Containerize the service.

## Architecture Philosophy

AP Auth Service is designed as an independently deployable service within the AP Self Storage ecosystem.

Each installation is intended for a single owner. Public registration and multi-user tenancy are not part of the current design.

Owner account creation will eventually be handled locally through an administrative CLI rather than a public registration endpoint.

The project is being developed with modularity, security, maintainability, and cross-platform deployment in mind.

---

**AP Self Storage — Authentication Service**
