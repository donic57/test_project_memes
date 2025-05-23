import requests
import allure
from endpoints.endpoint import Endpoint
from endpoints.delete_meme import DeleteMeme


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
            "info": ["driver", "driver2"]}
    ]

    @allure.step('Добавление мэма')
    def add_meme(self, authorize):
        body = {
            "text": "Спасибо всем народам, которые дружат за 3 выходных",
            "url": "https://www.memify.ru/meme/128787/",
            "tags": ["kotey", "andrey"],
            "info": {"description": "test_info"}
        }
        self.response = requests.post(
            self.url, headers=authorize, json=body)
        self.json = self.response.json()
        obj_id = self.json['id']
        print(f"Created object with ID: {obj_id}")
        try:
            yield obj_id, body  # Возвращаем оба значения
        finally:
            # Этот код выполнится после завершения работы с генератором
            DeleteMeme().delete_meme(obj_id, authorize)
            print(f"Deleting object with ID: {obj_id}")

    @allure.step('Проверка объектов в body и в ответе')
    def check_objs_in_meme(self, obj_id, body):
        if self.json is None:
            raise ValueError(
                "JSON response is None")
        assert self.json['text'] == body['text'], \
            f"Expected text {body['text']}, but got {self.json['text']}"
        assert self.json['url'] == body['url'], \
            (f"Expected url {body['url']}, "
             f"but got {self.json['url']}")
        assert self.json['tags'] == body['tags'], \
            (f"Expected tags {body['tags']}, "
             f"but got {self.json['tags']}")
        assert self.json['info'] == body['info'], \
            (f"Expected info {body['info']}, "
             f"but got {self.json['info']}")
        assert self.json['id'] == obj_id, \
            f'id {obj_id} нет в ответе'

    @allure.step(
        'Метод без генератора, просто отправляет запрос и проверяет 400')
    def add_bad_meme(self, authorize, body):
        self.response = requests.post(self.url, headers=authorize, json=body)
        return self
