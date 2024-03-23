from enum import Enum

from pydantic import BaseModel

from src.types import EntryId
from ..mixins import MixinId


class PracticeTitle(str, Enum):
    easy_yoga = "Легкая YOGA"
    elementary_middle_yoga = "YOGA начальный и средний"
    hatha_yoga = "Хатха YOGA"


class _PracticeBaseModel(BaseModel):
    # TODO: Вместо названия использовать перечисление возможных практик
    title: PracticeTitle
    description: str


class PracticeModel(_PracticeBaseModel):
    """Модель данных о практике"""

    id: EntryId


class CreatePracticeModel(MixinId, _PracticeBaseModel):
    """Модель данных для создания практики"""

    pass


class UpdatePracticeModel(BaseModel):
    """Модель данных для обновления данных о практике"""

    title: PracticeTitle | None = None
    description: str | None = None
