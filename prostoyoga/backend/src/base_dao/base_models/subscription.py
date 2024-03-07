from datetime import datetime, UTC

from pydantic import Field, BaseModel

from .mixins import MixinStartEndTime, MixinId


class SubscriptionModel(MixinId, MixinStartEndTime):
    """Модель для работы с абонементом (профилем пользователя)"""

    first_name: str
    second_name: str
    phone: str = Field(min_length=11, max_length=11)
    registration_date: datetime
    remaining_visits: int


class UpdateSubscriptionModel(BaseModel):
    """Модель для обновления данных абонемента (профиля пользователя)"""

    # TODO: добавить валидацию:
    #   - имя и фамилия должны быть длиннее 2 символов и содержать только буквы
    #   - телефон может быть только из 11 символов, если начинается с 8... или из 12, если с +7... (Сделать проверку цифр после 8/+7?)
    #   - дата начала занятий должна быть не меньше сегодняшней
    #   - кол-во оставшихся занятий должно быть не меньше 0
    first_name: str | None = None
    second_name: str | None = None
    phone: str | None = None
    remaining_visits: int | None = None
    start_at: datetime | None
    end_at: datetime | None


class CreateSubscriptionModel(MixinId, MixinStartEndTime):
    """Модель для создания абонемента пользователя"""

    # TODO: добавить валидацию:
    #   - имя и фамилия должны быть длиннее 2 символов и содержать только буквы
    #   - телефон может быть только из 11 символов, если начинается с 8... или из 12, если с +7... (Сделать проверку цифр после 8/+7?)
    #   - дата должна быть не меньше сегодняшней
    #   - кол-во оставшихся занятий должно быть не меньше 0
    first_name: str
    second_name: str
    phone: str = Field(min_length=11, max_length=12)
    registration_date: datetime = Field(default_factory=lambda: datetime.now(UTC))
    remaining_visits: int = Field(ge=0, default=0)
