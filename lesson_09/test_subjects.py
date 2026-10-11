import pytest
from sqlalchemy import text

# Тестовые данные для изоляции тестов
TEST_SUBJECT_ID = 999
TEST_SUBJECT_TITLE = "Автотестирование"
NEW_SUBJECT_TITLE = "Продвинутое автотестирование"


@pytest.fixture(autouse=True)
def clean_up(db_connection):
    """Фикстура очистки: удаляет тестовые данные ДО и ПОСЛЕ теста."""
    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    )
    db_connection.commit()
    yield
    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    )
    db_connection.commit()


def test_add_subject(db_connection):
    """1. Тест на ДОБАВЛЕНИЕ предмета."""
    db_connection.execute(
        text("""
        INSERT INTO subject (" \"subject_id, subject_title)
          VALUES (:id, :title)"
        """),
        {"id": TEST_SUBJECT_ID, "title": TEST_SUBJECT_TITLE}
    )
    db_connection.commit()

    result = db_connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    ).fetchone()

    assert result is not None, "Запись не найдена в БД"
    assert result[0] == TEST_SUBJECT_TITLE


def test_update_subject(db_connection):
    """2. Тест на ИЗМЕНЕНИЕ предмета."""
    db_connection.execute(
        text("""
        INSERT INTO subject (subject_id, subject_title)
        VALUES (:id, :title)
        """),
        {"id": TEST_SUBJECT_ID, "title": TEST_SUBJECT_TITLE}
    )
    db_connection.commit()

    db_connection.execute(
        text("""
             UPDATE subject
             SET subject_title = :new_title
             WHERE subject_id = :id"
            """),
        {"id": TEST_SUBJECT_ID, "new_title": NEW_SUBJECT_TITLE}
    )
    db_connection.commit()

    result = db_connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    ).fetchone()

    assert result[0] == NEW_SUBJECT_TITLE


def test_delete_subject(db_connection):
    """3. Те sun на УДАЛЕНИЕ предмета."""
    db_connection.execute(
        text("""INSERT INTO subject (subject_id, subject_title)
          VALUES (:id, :title)
          """),
        {"id": TEST_SUBJECT_ID, "title": TEST_SUBJECT_TITLE}
    )
    db_connection.commit()

    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    )
    db_connection.commit()

    result = db_connection.execute(
        text("SELECT * FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    ).fetchone()

    assert result is None, "Запись осталась в БД после удаления"
