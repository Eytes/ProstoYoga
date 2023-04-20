from sqlalchemy.orm import Session

from database import engine
from database.models import Client


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
