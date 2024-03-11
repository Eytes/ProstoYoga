import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class MongoSettings(BaseModel):
    username: str = os.getenv("MONGO_USERNAME")  # type: ignore
    password: str = os.getenv("MONGO_PASSWORD")  # type: ignore
    port: str = os.getenv("PORT")  # type: ignore
    host: str = os.getenv("HOST")  # type: ignore
    db_name: str = os.getenv("DB_NAME")  # type: ignore
    default_url: str = f"mongodb://{username}:{password}@{host}:{port}/{db_name}"


class RegistrySettings(BaseSettings):
    mongo: MongoSettings = MongoSettings()


registry_settings = RegistrySettings()
