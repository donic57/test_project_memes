import allure
import pytest


class Endpoint:

    def __init__(self):
        self.url = 'http://167.172.172.115:52355/meme'
        self.url_autorize = 'http://167.172.172.115:52355/authorize'
        self.response = None
        self.json = None

    @allure.step('Проверка на код ответа 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверка на код ответа 401')
    def check_status_is_401(self):
        status = self.response.status_code
        print(f'Ошибка с код {status} т.к. неавторизованный пользователь')
        assert status == 401
        pytest.xfail("Тест принудительно помечен как ожидаемо проваленный")

    @allure.step('Проверка на код ответа 400')
    def check_status_is_400(self):
        status = self.response.status_code
        print(f'Ошибка с код {status} переданы некорректные данные в запрос')
        assert status == 400
        pytest.xfail("Тест принудительно помечен как ожидаемо проваленный")

    @allure.step('Проверка на код ответа 404')
    def check_status_is_404(self):
        status = self.response.status_code
        print(f'Ошибка с код {status} переданы некорректные данные в запрос')
        assert status == 404
        pytest.xfail("Тест принудительно помечен как ожидаемо проваленный")

    @allure.step('Проверка на код ответа 404 с неcуществующим id')
    def check_noid_status_is_404(self, response, meme_id):
        status = response.status_code
        assert status == 404, \
            f"Мем с id={meme_id} всё ещё существует! Код: {status}"
        print(f'Ошибка с код {status} такой id не существует')

    @allure.step('Проверка объектов в ответе и в body')
    def check_objs_in_body(self, meme_id, body):
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
        assert int(self.json['id']) == meme_id, \
            (f"Expected id {meme_id}, "
             f"but got {self.json['id']}")
