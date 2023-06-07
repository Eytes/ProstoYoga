from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class RoleType(Enum):
    admin = 'admin'
    user = 'user'
    coach = 'coach'


class User(BaseModel):
    id: int
    name: str = Field(min_length=2)
    lastname: Optional[str]
    patronymic: Optional[str]
    phone: Optional[str]
    role: RoleType


class Training(BaseModel):
    id: int
    day: int = Field(ge=1, le=31)
    month: int = Field(ge=1, le=12)
    year: int = Field(ge=0)
    time: int = Field(ge=0)
