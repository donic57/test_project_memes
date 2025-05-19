import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.step('Создаем переменную body')
    def update_body(self, crate_meme_id):
        body = {
            "id": crate_meme_id,
            "text": "im driver",
            "url": "https://www.memify.ru/meme/142950/im-driver/",
            "tags": ["driver", "driver2"],
            "info": {"description": "test_info", "color": "pink"}
        }
        return body


    @allure.step('Обновление мэмов по id')
    def update_meme(self, crate_meme_id, authorize, body):
        self.response = requests.put(
            f'{self.url}/{crate_meme_id}', headers=authorize, json=body)
        self.json = self.response.json()
        return self.json
