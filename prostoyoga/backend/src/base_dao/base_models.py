from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from .base_types import EntryId


class _MixinId(BaseModel):
    id: EntryId = Field(default_factory=lambda: uuid4().hex)


class _MixinStartEndTime(BaseModel):
    start_at: datetime
    end_at: datetime


class PracticeModel(_MixinId, _MixinStartEndTime):
    # TODO: тип практики?
    master_id: EntryId
    title: str


class SubscriptionModel(_MixinId, _MixinStartEndTime):
    user_id: EntryId
    remaining_visits: int = Field(ge=0, default=0)


class UserModel(_MixinId):
    first_name: str = Field(min_length=2)
    second_name: str = Field(min_length=2)
    phone: str = Field(min_length=11, max_length=11)
