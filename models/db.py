from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db:5432/users_db"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,           # максимальное количество подключений
    max_overflow=5,         # сколько дополнительных подключений можно создать при необходимости
    pool_timeout=30,        # сколько секунд ждать свободное подключение
    pool_recycle=1800       # перезапуск соединения каждые 30 минут (во избежание "stale connections")
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
