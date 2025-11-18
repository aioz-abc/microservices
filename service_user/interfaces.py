from abc import ABC, abstractmethod
from common.schemas import UserCreate, UserRead

class IUserService(ABC):
    @abstractmethod
    def create_user(self, data: UserCreate) -> UserRead:
        pass

    @abstractmethod
    def list_users(self) -> list[UserRead]:
        pass
