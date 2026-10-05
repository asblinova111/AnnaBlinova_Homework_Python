import random
import pytest
from yougile_api import YougileApi

# --- ДАННЫЕ ДЛЯ АВТОРИЗАЦИИ (ЗАПОЛНЯЮТСЯ НАСТАВНИКОМ) ---
TOKEN = "5KXxZUNyGO3hnqiEoHnK2WDnXv+Y3fJJtF-ZR4q2ayHpbMbeKW4obsNSfpvAVQlb"
COMPANY_ID = "bc744177-d4b0-4238-b04e-aecbe950c1a1"


@pytest.fixture
def api():
    # Фикстура создает объект нашего API-клиента перед каждым тестом
    return YougileApi(token=TOKEN, company_id=COMPANY_ID)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [POST] /api-v2/projects (Создание проекта)
# =====================================================================

def test_create_project_positive(api):
    """Позитивный тест: Создание проекта с валидным названием"""
    unique_title = f"Автотест Проект Новый {random.randint(1, 999)}"
    response = api.create_project(title=unique_title)
    assert response.status_code == 201
    response_json = response.json()
    assert "id" in response_json


def test_create_project_negative_missing_title(api):
    """Негативный тест: Создание проекта без обязательного поля title"""
    # Передаем пустой словарь вместо названия
    response = api.create_project(title="", payload={})
    assert response.status_code == 400


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [GET] /api-v2/projects/{id} (Получение проекта)
# =====================================================================

def test_get_project_positive(api):
    """Позитивный тест: Получение существующего проекта по его реальному ID"""
    # Создаем проект с уникальным именем, чтобы избежать дубликатов Yougile
    unique_title = f"Проект для проверки GET {random.randint(1, 999)}"
    create_res = api.create_project(title=unique_title)
    project_id = create_res.json()["id"]

    # Запрашиваем информацию о созданном проекте
    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["title"] == unique_title


def test_get_project_negative_invalid_id(api):
    """Негативный тест: Попытка получить проект по несуществующему ID"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(non_existent_id)

    assert response.status_code == 404


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [PUT] /api-v2/projects/{id} (Обновление проекта)
# =====================================================================

def test_update_project_positive(api):
    """Позитивный тест: Успешное изменение названия существующего проекта"""
    # 1. Создаем проект
    create_res = api.create_project(title="Старое название")
    project_id = create_res.json()["id"]

    # 2. Обновляем его название на уникальное
    new_unique_title = f"Новое название автотеста {random.randint(1, 999)}"
    response = api.update_project(project_id, new_title=new_unique_title)

    assert response.status_code == 200

    # 3. Проверяем через GET, что имя на сервере действительно изменилось
    get_res = api.get_project(project_id)
    assert get_res.json()["title"] == new_unique_title


def test_update_project_negative_non_existent_id(api):
    """Негативный тест: Попытка обновить проект с фейковым ID"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(
        non_existent_id, new_title="Попытка обновления"
        )

    assert response.status_code == 404
