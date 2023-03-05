from dataclasses import dataclass
from src.entities.user import UserEntity


@dataclass
class GetUserRequest:
    user_id: str


@dataclass
class GetUserResponse:
    user: UserEntity
