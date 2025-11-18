from .interfaces import IUserService
from common.schemas import UserCreate, UserRead

class UserService(IUserService):
    def __init__(self):
        self._users = []
        self._id = 1

    def create_user(self, data: UserCreate) -> UserRead:
        user = UserRead(id=self._id, email=data.email)
        self._users.append(user)
        self._id += 1
        return user

    def list_users(self) -> list[UserRead]:
        return self._users
