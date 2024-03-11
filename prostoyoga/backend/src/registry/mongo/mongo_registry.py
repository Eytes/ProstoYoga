from typing import Sequence

from motor.core import AgnosticCollection

from src.types import EntryId
from ..abstract_registry import AbstractRegistry
from ..registry_types import RegistryQuery, RegistryData


class MongoRegistry(AbstractRegistry):

    def __init__(self, collection: AgnosticCollection) -> None:
        self.__collection = collection

    async def create(self, data: RegistryData) -> EntryId:
        """
        Создать документ в коллекции
        :param data: параметры нового документа
        :return: id документа
        """
        inserted_id = await self.__collection.insert_one(data)
        return EntryId(inserted_id)

    async def get(
        self,
        query: RegistryQuery,
        skip: int | None = None,
        limit: int | None = None,
    ) -> Sequence[RegistryData]:
        """
        Получить набор документов из коллекции
        :param query: параметры для выборки
        :param skip: количество пропущенных документов. По умолчанию 0
        :param limit: количество выданных документов. По умолчанию 1
        :return: набор документов, соответствующих параметрам выборки
        """
        skip = skip if skip is not None and skip > 0 else 0
        limit = limit if limit is not None and limit > 1 else 1
        return await self.__collection.find(query).skip(skip).to_list(limit)

    async def update(self, query: RegistryQuery, data: RegistryData) -> int:
        """
        Обновить документы из коллекции, соответствующие выборке
        :param query: параметры для выборки
        :param data: параметры для обновления
        :return: количество обновленных документов
        """
        return (
            await self.__collection.update_many(query, {"$set": data})
        ).modified_count

    async def delete(self, query: RegistryQuery) -> int:
        """
        Удалить документы, соответствующие выборке
        :param query: параметры для выборки
        :return: количество удаленных документов
        """
        return (await self.__collection.delete_many(query)).deleted_count
