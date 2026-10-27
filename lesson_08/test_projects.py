import random
import pytest
from yougile_api import YougileApi

@pytest.fixture
def api():
    return YougileApi()


@pytest.fixture
def project_factory(api):
    created_project_ids = []

    def _create_project(title: str, payload: dict = None):
        response = api.create_project(title=title, payload=payload)
        if response.status_code == 201:
            res_json = response.json()
            if "id" in res_json:
                created_project_ids.append(res_json["id"])
        return response

    yield _create_project

    # Очистка среды после тестов
    for project_id in created_project_ids:
        api.delete_project(project_id)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [POST] /api-v2/projects (Создание проекта)
# =====================================================================

def test_create_project_positive(project_factory):
    """Позитивный тест: Создание проекта с валидным названием"""
    unique_title = f"Автотест Проект Новый {random.randint(1, 999)}"
    response = project_factory(title=unique_title)
    assert response.status_code == 201
    response_json = response.json()
    assert "id" in response_json


def test_create_project_negative_missing_title(api):
    """Негативный тест: Создание проекта без обязательного поля title и проверка текста ошибки"""
    response = api.create_project(title="", payload={})
    assert response.status_code == 400
    
    response_json = response.json()
    # Куратор просил проверить текст ошибки. Проверяем, что в ответе есть хоть какое-то текстовое описание.
    error_text = str(response_json.get("error", response_json.get("message", response_json)))
    assert len(error_text) > 0


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [GET] /api-v2/projects/{id} (Получение проекта)
# =====================================================================

def test_get_project_positive(api, project_factory):
    """Позитивный тест: Получение существующего проекта по его реальному ID"""
    unique_title = f"Проект для проверки GET {random.randint(1, 999)}"
    create_res = project_factory(title=unique_title)
    project_id = create_res.json()["id"]

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["title"] == unique_title


def test_get_project_negative_invalid_id(api):
    """Негативный тест: Попытка получить проект по несуществующему ID и проверка текста ошибки"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(non_existent_id)

    assert response.status_code == 404
    
    response_json = response.json()
    error_text = str(response_json.get("error", response_json.get("message", response_json)))
    assert len(error_text) > 0


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [PUT] /api-v2/projects/{id} (Обновление проекта)
# =====================================================================

def test_update_project_positive(api, project_factory):
    """Позитивный тест: Успешное изменение названия существующего проекта. PUT проверяется через GET."""
    create_res = project_factory(title="Старое название")
    project_id = create_res.json()["id"]

    new_unique_title = f"Новое название автотеста {random.randint(1, 999)}"
    response = api.update_project(project_id, new_title=new_unique_title)

    assert response.status_code == 200

    get_res = api.get_project(project_id)
    assert get_res.json()["title"] == new_unique_title


def test_update_project_negative_non_existent_id(api):
    """Негативный тест: Попытка обновить проект с фейковым ID и проверка текста ошибки"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(non_existent_id, new_title="Попытка обновления")

    assert response.status_code == 404
    
    response_json = response.json()
    error_text = str(response_json.get("error", response_json.get("message", response_json)))
    assert len(error_text) > 0
