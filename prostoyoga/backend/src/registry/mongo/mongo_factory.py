import os

from motor.core import AgnosticClient, AgnosticCollection, AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient

from .mongo_registry import MongoRegistry


class MongoRegistryFactory:
    def __init__(self, mongo_client: AgnosticClient | None = None) -> None:
        if mongo_client is not None:
            self.__mongo_client: AgnosticClient = mongo_client
        else:
            username = os.getenv("MONGO_USERNAME")
            password = os.getenv("MONGO_PASSWORD")
            port = os.getenv("PORT")
            host = os.getenv("HOST")
            self.__mongo_client = AsyncIOMotorClient(
                f"mongodb://{username}:{password}@{host}:{port}"
            )
        db_name = os.getenv("DB_NAME")
        self.__database: AgnosticDatabase = self.__mongo_client[db_name]

    def get(self, collection_name: str) -> MongoRegistry:
        collection: AgnosticCollection = self.__database.get_collection(collection_name)
        return MongoRegistry(collection)
