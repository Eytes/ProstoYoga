from pydantic import BaseModel

from src.types import EntryId
from ..mixins import MixinId


class _PracticeBaseModel(BaseModel):
    # TODO: Вместо названия использовать перечисление возможных практик
    title: str
    description: str


class PracticeModel(_PracticeBaseModel):
    """Модель данных о практике"""

    id: EntryId


class CreatePracticeModel(MixinId, _PracticeBaseModel):
    """Модель данных для создания практики"""

    pass


class UpdatePracticeModel(BaseModel):
    """Модель данных для обновления данных о практике"""

    title: str | None = None
    description: str | None = None
