from abc import ABC, abstractmethod
from datetime import datetime
from typing import Iterable

from ..schedule.models import (
    UpdatePracticeInScheduleModel,
    PracticeInScheduleModel,
    CreatePracticeInScheduleModel,
)
from ..subscriptions.models import SubscriptionModel
from ..types import EntryId


class ScheduleInterfaces(ABC):
    @abstractmethod
    async def get_practices_in_the_period(
        self,
        start_at: datetime,
        end_at: datetime,
    ) -> Iterable[PracticeInScheduleModel]:
        # TODO: добавить фильтр по типу практик
        """
        Получить практики за период от start_at до end_at включительно
        """
        pass

    @abstractmethod
    async def add_practice(
        self,
        practice_data: CreatePracticeInScheduleModel,
    ) -> EntryId:
        """
        Внести запись о практике в расписание.
        Возвращается id записи в расписании
        """
        pass

    @abstractmethod
    async def delete_practice(self, schedule_entry_id: EntryId) -> EntryId:
        """
        Удалить запись о практике из расписания.
        Возвращается id удаленной записи в расписании
        """
        pass

    @abstractmethod
    async def update_practice(
        self,
        schedule_entry_id: EntryId,
        practice_data: UpdatePracticeInScheduleModel,
    ) -> EntryId:
        """
        Обновить данные о практике из расписания.
        Возвращает id обновленной записи в расписании
        """
        pass

    @abstractmethod
    async def register_the_subscription_by_id(
        self,
        schedule_entry_id: EntryId,
        subscription_id: EntryId,
    ) -> None:
        """Записать абонемент на практику из расписания"""
        pass

    @abstractmethod
    async def remove_the_subscription_by_id(
        self,
        schedule_entry_id: EntryId,
        subscription_id: EntryId,
    ) -> None:
        """Снять запись абонемента с практики из расписания"""
        pass

    @abstractmethod
    async def get_registered_subscriptions(
        self,
        schedule_entry_id: EntryId,
    ) -> Iterable[SubscriptionModel]:
        """Получить абонементы, записавшиеся на занятие"""
        pass

    @abstractmethod
    async def get_master_of_schedule_entry(self, schedule_entry_id: EntryId):
        """
        Получить данные о мастере, который будет проводить запланированную практику
        """
        # TODO: придумать модели для мастеров
        pass
