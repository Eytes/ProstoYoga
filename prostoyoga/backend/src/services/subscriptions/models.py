from datetime import datetime, UTC

from pydantic import Field, BaseModel, constr, validator

from src.types import EntryId
from ..mixins import MixinStartEndTime, MixinId


class PhoneNumber(BaseModel):
    number: constr(min_length == 11, max_length == 12)

    @validator("number")
    def validate_phone_number(cls, phone_number):
        # Проверка длины номера и начала (8 или +7)
        if len(phone_number) == 11 and phone_number.startswith("8"):
            return phone_number[1:]
        elif len(phone_number) == 12 and phone_number.startswith("+7"):
            return phone_number[2:]
        else:
            raise ValueError("Неверный формат номера телефона")


class _SubscriptionBaseModel(MixinStartEndTime, BaseModel):
    """Базовые поля, содержащиеся во всех моделях абонемента"""

    first_name: str = Field(min_length=3)
    second_name: str = Field(min_length=3)
    phone: PhoneNumber.number
    remaining_visits: int = Field(ge=0, default=0)


class SubscriptionModel(_SubscriptionBaseModel):
    """Модель для работы с абонементом (профилем пользователя)"""

    id: EntryId
    registration_date: datetime


class CreateSubscriptionModel(MixinId, _SubscriptionBaseModel):
    """Модель для создания абонемента пользователя"""

    registration_date: datetime = Field(default_factory=lambda: datetime.now(UTC))


class UpdateSubscriptionModel(BaseModel, _SubscriptionBaseModel):
    """Модель для обновления данных абонемента (профиля пользователя)"""

    start_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    end_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
