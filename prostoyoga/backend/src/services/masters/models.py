from pydantic import BaseModel

from src.types import EntryId
from ..mixins import MixinId


class _MasterBaseModel(BaseModel):
    first_name: str
    second_name: str
    phone: str


class MasterModel(_MasterBaseModel):
    """Модель данных мастера"""

    id: EntryId


class CreateMasterModel(MixinId, _MasterBaseModel):
    """Модель данных для создания мастера"""

    pass


class UpdateMasterModel(BaseModel):
    """Модель данных для обновления данных о мастере"""

    first_name: str | None = None
    second_name: str | None = None
    phone: str | None = None
