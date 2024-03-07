from abc import ABC, abstractmethod

from .base_models.practice import (
    PracticeModel,
    CreatePracticeModel,
    UpdatePracticeModel,
)
from .base_types import EntryId


class PracticesDAO(ABC):
    @abstractmethod
    async def get_by_id(self, practice_id: EntryId) -> PracticeModel:
        """Получить данные о практике"""
        pass

    @abstractmethod
    async def create(self, new_practice: CreatePracticeModel) -> EntryId:
        """Создать новую практику. Возвращает id новой практики"""
        pass

    @abstractmethod
    async def delete_by_id(self, practice_id: EntryId) -> EntryId:
        """Удалить практику. Возвращает id удаленной практики"""
        pass

    @abstractmethod
    async def update(self, new_practice_data: UpdatePracticeModel) -> EntryId:
        """Обновление данных о практике. Возвращает id обновленной практики"""
        pass
