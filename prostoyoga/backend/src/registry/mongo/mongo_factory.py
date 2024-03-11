from motor.core import AgnosticClient, AgnosticCollection, AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient

from .mongo_registry import MongoRegistry
from ..registry_config import registry_settings


class MongoRegistryFactory:
    def __init__(self, mongo_client: AgnosticClient | None = None) -> None:
        if not mongo_client:
            mongo_client = AsyncIOMotorClient(registry_settings.mongo.default_url)

        self.__mongo_client: AgnosticClient = mongo_client
        self.__database: AgnosticDatabase = self.__mongo_client[
            registry_settings.mongo.db_name
        ]

    def get(self, collection_name: str) -> MongoRegistry:
        collection: AgnosticCollection = self.__database.get_collection(collection_name)
        return MongoRegistry(collection)
