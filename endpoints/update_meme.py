import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    TEST_DATA = [{"id": '354',
                  "text": "test_text",
                  "url": "https://ya.ru/",
                  "tags": ["test_driver", "test_driver2"],
                  "info": {"description": "sdfsdfo", "color": "sdfsdf"}},
                 {"id": 354,
                  "text": 12345,
                  "url": "https://ya.ru/",
                  "tags": ["test_driver", "test_driver2"],
                  "info": {"description": "sdfsdfo", "color": "sdfsdf"}},
                 {"id": 354,
                  "text": "test_text",
                  "url": "https://ya.ru/",
                  "tags": "test_driver2",
                  "info": {"description": "sdfsdfo", "color": "sdfsdf"}},
                 {"id": 354,
                  "text": "test_text",
                  "url": "https://ya.ru/",
                  "tags": ["test_driver", "test_driver2"],
                  "info": ["driver", "driver2"]}
                 ]

    @allure.step('Создаем переменную body')
    def update_body(self, meme_id):
        body = {
            "id": meme_id,
            "text": "im driver",
            "url": "https://www.memify.ru/meme/142950/im-driver/",
            "tags": ["driver", "driver2"],
            "info": {"description": "test_info", "color": "pink"}
        }
        return body

    @allure.step('Обновление мэмов по id')
    def update_meme(self, meme_id, authorize, body):
        self.response = requests.put(
            f'{self.url}/{meme_id}', headers=authorize, json=body)
        self.json = self.response.json()
        return self.json

    def bad_update_body(self, authorize, body):
        meme_id = 354
        self.response = requests.put(
            f'{self.url}/{meme_id}', headers=authorize, json=body)
        return self.response
