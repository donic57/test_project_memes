import requests
import allure
from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):

    TEST_DATA = [
        {
            "text": 12345,
            "url": "https://ya.ru/",
            "tags": ["test_driver", "test_driver2"],
            "info": {"description": "sdfsdfo", "color": "sdfsdf"}},
        {
            "text": "test_text",
            "url": "https://ya.ru/",
            "tags": "test_driver2",
            "info": {"description": "sdfsdfo", "color": "sdfsdf"}},
        {
            "text": "test_text",
            "url": "https://ya.ru/",
            "tags": ["test_driver", "test_driver2"],
            "info": ["driver", "driver2"]},
    ]

    TEST_DATA_OK = [
        {
            "text": "",
            "url": "https://ya.ru/",
            "tags": ["test_driver", "test_driver2"],
            "info": {"description": "test_info"}
        },
        {
            "text": "test_text",
            "url": "",
            "tags": ["test_driver", "test_driver2"],
            "info": {"description": "test_info"}
        }
    ]

    @allure.step('Добавление мэма')
    def add_meme(self, authorize=None, body=None, expected_status=True):
        if body is None:
            body = {
                "text": "Спасибо всем народам, которые дружат за 3 выходных",
                "url": "https://www.memify.ru/meme/128787/",
                "tags": ["kotey", "andrey"],
                "info": {"description": "test_info"}
            }
        if authorize is None:
            self.response = requests.post(self.url, json=body)
        else:
            self.response = requests.post(
                self.url, headers=authorize, json=body)
        if not expected_status:
            return self  # Для негативных тестов возвращаем self напрямую
        if not self.response.ok:
            return self  # Для неудачных запросов возвращаем self
        try:
            self.json = self.response.json()
            obj_id = self.json['id']
            print(f"Created object with ID: {obj_id}")
            return self  # Для успешных запросов возвращаем self
        except (ValueError, KeyError) as e:
            print(f"Failed to parse response: {e}")
            return self
