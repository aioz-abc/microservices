from abc import ABC, abstractmethod
from pydantic import BaseModel, EmailStr


class RegisterSchema(BaseModel):
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    message: str
    token: str | None = None


class IAuthService(ABC):

    @abstractmethod
    def login(self, data: LoginSchema) -> AuthResponse:
        pass

    @abstractmethod
    def register(self, data: RegisterSchema) -> AuthResponse:
        pass
