from abc import ABC, abstractmethod

from src.types import EntryId
from .models import (
    SubscriptionModel,
    CreateSubscriptionModel,
    UpdateSubscriptionModel,
)


class MastersInterfaces(ABC):
    @abstractmethod
    async def get_by_id(self, subscription_id: EntryId) -> SubscriptionModel:
        """Получить данные абонемента"""
        pass

    @abstractmethod
    async def create(self, new_subscription: CreateSubscriptionModel) -> EntryId:
        """Создать новый абонемент. Возвращает id нового абонемента"""
        pass

    @abstractmethod
    async def delete_by_id(self, subscription_id: EntryId) -> EntryId:
        """Удалить абонемент. Возвращает id удаленного абонемента"""
        pass

    @abstractmethod
    async def update(self, new_subscription_data: UpdateSubscriptionModel) -> EntryId:
        """Обновление данных абонемента. Возвращает id обновленного абонемента"""
        pass
