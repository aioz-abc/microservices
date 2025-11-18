from .interfaces import IUserService
from .service_impl import UserService

_user_service: IUserService | None = None

def init_dependencies():
    global _user_service
    _user_service = UserService()
    print("UserService initialized")

def get_user_service() -> IUserService:
    if _user_service is None:
        raise Exception("User service not initialized")
    return _user_service
