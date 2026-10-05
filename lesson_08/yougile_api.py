import requests


class YougileApi:

    def __init__(self, token: str, company_id: str):
        self.base_url = "https://ru.yougile.com/api-v2"
        # Формируем заголовки для авторизации по API-документации Yougile
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        # Идентификатор компании часто передается в заголовках или параметрах
        if company_id:
            self.headers["yougile-company-id"] = company_id

    # 1. Метод [POST] /api-v2/projects — Создание проекта
    def create_project(
            self, title: str, payload: dict = None) -> requests.Response:
        url = f"{self.base_url}/projects"
        if payload is None:
            payload = {"title": title}

        response = requests.post(url, json=payload, headers=self.headers)
        return response

    # 2. Метод [GET] /api-v2/projects/{id} — Получение проекта по ID
    def get_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    # 3. Метод [PUT] /api-v2/projects/{id} — Изменение проекта по ID
    def update_project(
            self, project_id: str, new_title: str
            ) -> requests.Response:
        url = f"{self.base_url}/projects/{project_id}"
        payload = {"title": new_title}
        response = requests.put(url, json=payload, headers=self.headers)
        return response
