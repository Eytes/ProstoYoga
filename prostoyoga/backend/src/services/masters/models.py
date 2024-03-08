from pydantic import BaseModel

from ..mixins import MixinId
from ..types import EntryId


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


class UpdateMasterModel(_MasterBaseModel):
    """Модель данных для обновления данных о мастере"""

    first_name: str | None = None
    second_name: str | None = None
    phone: str | None = None
