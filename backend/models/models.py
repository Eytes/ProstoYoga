from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    lastname: str
    patronymic: str
    phone: str
