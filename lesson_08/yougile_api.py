import os
import requests
from dotenv import load_dotenv

# Находим точный путь к файлу .env, который лежит в той же папке
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')

# Загружаем переменные окружения строго по вычисленному пути
load_dotenv(dotenv_path=env_path)

class YougileApi:

    def __init__(self, token: str = None, company_id: str = None):
        # Базовый адрес хоста
        self.base_url = "https://yougile.com"
        
        # Считываем скрытые данные из .env
        active_token = token or os.getenv("YOUGILE_TOKEN")
        active_company_id = company_id or os.getenv("COMPANY_ID")
        
        # Формируем заголовки авторизации
        self.headers = {
            "Authorization": f"Bearer {active_token}",
            "Content-Type": "application/json"
        }
        
        # Передаем идентификатор компании в заголовки
        if active_company_id:
            self.headers["yougile-company-id"] = active_company_id

    # 1. Метод [POST] /api-v2/projects — Создание проекта
    def create_project(
            self, title: str, payload: dict = None) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects"
        if payload is None:
            payload = {"title": title}

        response = requests.post(url, json=payload, headers=self.headers)
        return response

    # 2. Метод [GET] /api-v2/projects/{id} — Получение проекта по ID
    def get_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    # 3. Метод [PUT] /api-v2/projects/{id} — Изменение проекта по ID
    def update_project(
            self, project_id: str, new_title: str
            ) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"title": new_title}
        response = requests.put(url, json=payload, headers=self.headers)
        return response

    # 4. Метод [PUT] /api-v2/projects/{id} — Мягкое удаление проекта
    def delete_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"deleted": True}
        response = requests.put(url, json=payload, headers=self.headers)
        return response
