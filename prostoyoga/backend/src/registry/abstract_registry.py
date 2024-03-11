from abc import ABC, abstractmethod
from typing import Sequence

from .registry_types import RegistryData, RegistryQuery
from ..types import EntryId


class AbstractRegistry(ABC):
    @abstractmethod
    async def create(self, data: RegistryData) -> EntryId:
        """
        Создание записи в БД на основе параметров в data

        Возвращается id новой записи
        """
        pass

    @abstractmethod
    async def get(self, query: RegistryQuery) -> Sequence[RegistryData]:
        """
        Получить записи из БД по параметрам из query

        Возвращается последовательность из набора подходящих записей
        """
        pass

    @abstractmethod
    async def update(self, query: RegistryQuery, data: RegistryData) -> int:
        """
        Обновить запись в БД:
        - Поиск записи по значениям из параметров query
        - Новые данные из параметров data

        Возвращается количество обновленных записей
        """
        pass

    @abstractmethod
    async def delete(self, query: RegistryQuery) -> int:
        """
        Удаление записей из БД, по фильтру query

        Возвращается количество удаленных записей
        """
        pass
