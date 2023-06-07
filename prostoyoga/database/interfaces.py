from sqlalchemy.orm import Session

from prostoyoga.database import engine
from prostoyoga.database.tables import Client


def clients(limit: int = 10, offset: int = 0):
    with Session(autoflush=False, bind=engine) as db:
        return db.query(Client).offset(offset).limit(limit).all()


def create_client(name: str, lastname: str, phone: str, patronymic: str | None = None):
    with Session(autoflush=False, bind=engine) as db:
        if patronymic:
            new_client = Client(name=name, lastname=lastname, patronymic=patronymic, phone=phone)
        else:
            new_client = Client(name=name, lastname=lastname, phone=phone)
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client.id


def last_client_visit():
    ...


def client_visits():
    ...


def subscription_purchase_day():
    ...


def remaining_training():
    ...


def subscription_end():
    ...


def buy_subscription():
    ...


def close_subscription():
    ...


def update_subscription():
    ...


def mark_visit():
    ...


def cancel_visit():
    ...
