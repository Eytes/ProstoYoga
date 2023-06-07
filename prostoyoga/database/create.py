from sqlalchemy.engine import create_engine, Engine

from ProstoYoga.config import DATABASE_URL
from ProstoYoga.database import create_models


def create_database() -> Engine:
    # TODO: проверить существование БД. Если существует, то проверить структуру, иначе - пересоздать
    if 'sqlite' in DATABASE_URL:
        '''По умолчанию SQLite разрешает взаимодействовать с БД только одному потоку, но в FastAPI 
        в рамках одного и того же запроса с базой данных могут взаимодействовать более одного потока, 
        поэтому необходима подобная настройка для получения необходимых разрешений. При этом каждый 
        запрос будет получать свой собственный сеанс подключения к базе данных через механизм внедрения зависимостей'''
        eng: Engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
    else:
        eng: Engine = create_engine(DATABASE_URL, echo=True)

    create_models(eng)
    return eng


engine = create_database()
