from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from database import create_models


def setup() -> Engine:
    if 'sqlite' in DATABASE_URL:
        '''По умолчанию SQLite разрешает взаимодействовать с БД только одному потоку, но в FastAPI 
        в рамках одного и того же запроса с базой данных могут взаимодействовать более одного потока, 
        поэтому необходима подобная настройка для получения необходимых разрешений. При этом каждый 
        запрос будет получать свой собственный сеанс подключения к базе данных через механизм внедрения зависимостей'''
        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
    else:
        engine = create_engine(DATABASE_URL, echo=True)

    create_models(engine)
    return engine

Session = sessionmaker(autoflush=False, bind=setup())
