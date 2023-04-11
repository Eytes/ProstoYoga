from sqlalchemy import Integer, String, DateTime
from sqlalchemy import Column
from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine import Engine


class Base(DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer())
    name = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)
    patronymic = Column(String())
    phone = Column(String(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='client_pk'),
        UniqueConstraint('phone')
    )


class Coach(Base):
    __tablename__ = 'coaches'

    id = Column(Integer())
    name = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)
    patronymic = Column(String())
    phone = Column(String(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='coach_pk'),
        UniqueConstraint('phone')
    )


class TrainingType(Base):
    __tablename__ = 'training_types'

    id = Column(Integer())
    title = Column(String(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='training_type_pk'),
        UniqueConstraint('title')
    )


class Training(Base):
    __tablename__ = 'trainings'

    id = Column(Integer())
    type_id = Column(Integer(), nullable=False)
    duration = Column(String(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='training_pk'),
        ForeignKeyConstraint(['type_id'], ['training_types.id'])
    )


class Schedule(Base):
    __tablename__ = 'schedule'

    date = Column(DateTime())
    time = Column(DateTime())
    coach_id = Column(Integer(), nullable=False)
    training_id = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('date', 'time', name='schedule_pk'),
        ForeignKeyConstraint(['coach_id'], ['coaches.id']),
        ForeignKeyConstraint(['training_id'], ['trainings.id'])
    )


class SubscriptionType(Base):
    __tablename__ = 'subscription_types'

    id = Column(Integer())
    praise = Column(Integer(), nullable=False)
    title = Column(String(), nullable=False)
    visits_number = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='subscription_type_pk'),
        UniqueConstraint('title')
    )


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer())
    client_id = Column(Integer(), nullable=False)
    subscription_type_id = Column(Integer(), nullable=False)
    remaining_training_number = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='subscription_pk'),
        ForeignKeyConstraint(['client_id'], ['clients.id']),
        ForeignKeyConstraint(['subscription_type_id'], ['subscription_types.id'])
    )


class Visit(Base):
    __tablename__ = 'visits'

    training_id = Column(Integer(), nullable=False)
    client_id = Column(Integer(), nullable=False)
    date = Column(DateTime(), nullable=False)
    time = Column(DateTime(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('client_id', 'date', 'time', name='visit_pk'),
    )


def create_models(engine: Engine):
    Base.metadata.create_all(bind=engine)
