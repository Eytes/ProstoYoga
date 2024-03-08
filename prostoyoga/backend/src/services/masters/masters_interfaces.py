from abc import ABC, abstractmethod

from .models import (
    MasterModel,
    CreateMasterModel,
    UpdateMasterModel,
)
from ..types import EntryId


class MastersInterfaces(ABC):
    @abstractmethod
    async def get_by_id(self, master_id: EntryId) -> MasterModel:
        """Получить данные о мастере"""
        pass

    @abstractmethod
    async def create(self, new_master: CreateMasterModel) -> EntryId:
        """Создать нового мастера. Возвращает id нового мастера"""
        pass

    @abstractmethod
    async def delete_by_id(self, master_id: EntryId) -> EntryId:
        """Удалить мастера. Возвращает id удаленного мастера"""
        pass

    @abstractmethod
    async def update(self, new_master_data: UpdateMasterModel) -> EntryId:
        """Обновление данных о мастере. Возвращает id обновленного мастера"""
        pass
