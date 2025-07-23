from abc import ABC, abstractmethod
import datetime

class UserRepositoryInterface(ABC):
    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def add_orders(self, user_id: int, description: str, date_order: datetime) -> None:
        pass

    @abstractmethod
    def get_user_orders(self,  username: str):
        pass
