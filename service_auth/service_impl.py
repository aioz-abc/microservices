import requests
from .interfaces import IAuthService, RegisterSchema, LoginSchema, AuthResponse

USER_SERVICE_URL = "http://127.0.0.1:8001/users"


class AuthService(IAuthService):

    def login(self, data: LoginSchema) -> AuthResponse:
        res = requests.get(f"{USER_SERVICE_URL}/by-email", params={"email": data.email})

        if res.status_code != 200:
            return AuthResponse(message="User not found", token=None)

        user = res.json()

        if user["password"] != data.password:
            return AuthResponse(message="Wrong password", token=None)

        token = f"fake-jwt-for-{data.email}"

        return AuthResponse(message="Login successful", token=token)

    def register(self, data: RegisterSchema) -> AuthResponse:
        payload = {"email": data.email, "password": data.password}

        res = requests.post(USER_SERVICE_URL, json=payload)

        if res.status_code != 200:
            return AuthResponse(message="User creation failed", token=None)

        token = f"fake-jwt-for-{data.email}"

        return AuthResponse(message="Registration successful", token=token)
