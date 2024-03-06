from abc import ABC, abstractmethod
from datetime import datetime
from typing import Iterable

from .base_models import PracticeModel, UserModel
from .base_types import EntryId


class PracticeDAO(ABC):
    @abstractmethod
    async def get_by_id(self, practice_id: EntryId) -> PracticeModel:
        """Получить данные о практике"""
        pass

    @abstractmethod
    async def get_in_the_period(
        self,
        start_at: datetime,
        end_at: datetime,
    ) -> Iterable[PracticeModel]:
        # TODO: добавить фильтр по типу практик
        """Получить практики за период"""
        pass

    @abstractmethod
    async def create(self, new_practice: PracticeModel) -> EntryId:
        """Внести практику в расписание"""
        pass

    @abstractmethod
    async def delete_by_id(self, practice_id: EntryId) -> EntryId:
        """Удалить практику из расписания"""
        pass

    @abstractmethod
    async def update(self, new_practice_data: PracticeModel) -> None:
        """Обновление данных о практике"""
        pass

    @abstractmethod
    async def register_the_user_by_id(
        self,
        user_id: EntryId,
        practice_id: EntryId,
    ) -> None:
        """Записать пользователя на практику"""
        pass

    @abstractmethod
    async def remove_the_user_by_id(
        self,
        user_id: EntryId,
        practice_id: EntryId,
    ) -> None:
        """Снять запись пользователя с практики"""
        pass

    @abstractmethod
    async def get_registered_users(self, practice_id: EntryId) -> Iterable[UserModel]:
        """Получить пользователей, записавшихся на занятие"""
        pass
