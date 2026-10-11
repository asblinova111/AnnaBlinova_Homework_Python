import pytest
from sqlalchemy import create_engine

# Замените ВАШ_ПАРОЛЬ на реальный пароль от pgAdmin
DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/QA"


@pytest.fixture(scope="session")
def db_engine():
    """Создает движок SQLAlchemy для подключения к БД."""
    engine = create_engine(DATABASE_URL)
    yield engine
    engine.dispose()


@pytest.fixture
def db_connection(db_engine):
    """Предоставляет чистое соединение для каждого теста."""
    connection = db_engine.connect()
    yield connection
    connection.close()
