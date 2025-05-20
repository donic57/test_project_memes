import requests
import allure
import pytest


class Endpoint:

    def __init__(self):
        self.url = 'http://167.172.172.115:52355/meme'
        self.response = None
        self.json = None

    @allure.step('Проверка на код ответа 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверка на код ответа 401')
    def check_status_is_401(self):
        status = self.response.status_code
        assert status == 401
        print(f'Ошибка с код {status} т.к. неавторизованный пользователь')
        pytest.xfail("Тест принудительно помечен как ожидаемо проваленный")

    @allure.step('Проверка на код ответа 400')
    def check_status_is_400(self):
        status = self.response.status_code
        assert status == 400
        print(f'Ошибка с код {status} переданы некорректные данные в запрос')
        pytest.xfail("Тест принудительно помечен как ожидаемо проваленный")

    @allure.step('Вызов get запроса без token')
    def get_memes_unauthorized(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.step('Проверка объектов в ответе и в body')
    def check_objs_in_body(self, body):
        if self.json is None:
            raise ValueError(
                "JSON response is None! Did you call get-method first?")
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
        assert 'id' in self.json
