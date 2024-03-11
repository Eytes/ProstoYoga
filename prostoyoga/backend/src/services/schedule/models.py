from datetime import datetime

from pydantic import BaseModel

from src.types import EntryId
from ..mixins import MixinStartEndTime, MixinId


class _PracticeInScheduleBaseModel(MixinStartEndTime):
    """Базовые поля, содержащиеся во всех моделях расписания"""

    practice_id: EntryId
    master_id: EntryId


class PracticeInScheduleModel(_PracticeInScheduleBaseModel):
    """
    Модель данных записи в расписании о проведении практики
    с мастером и указанием времени начала и конца проведения практики
    """

    id: EntryId


class CreatePracticeInScheduleModel(MixinId, _PracticeInScheduleBaseModel):
    """
    Модель данных для создания записи в расписании о проведении практики
    с мастером и указанием времени начала и конца проведения практики
    """

    pass


class UpdatePracticeInScheduleModel(BaseModel):
    """
    Модель данных для обновления записи в расписании о проведении практики
    с мастером и указанием времени начала и конца проведения практики
    """

    practice_id: EntryId | None = None
    master_id: EntryId | None = None
    start_at: datetime | None = None
    end_at: datetime | None = None
