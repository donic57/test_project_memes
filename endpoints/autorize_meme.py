import requests
import allure
import os
from endpoints.endpoint import Endpoint


class Authorize(Endpoint):

    @allure.step('Авторизация пользователя')
    def user_authorize(self):
        base_way = os.path.dirname(__file__)
        token_file_way = os.path.dirname(base_way)
        token_data = os.path.join(
            token_file_way, 'tests', 'token_file')
        body = {"name": "lyadov"}

        # Читаем текущий токен из файла
        with open(token_data, 'r') as data_file:
            token = data_file.readline().strip()

        # Проверяем токен
        self.response = requests.get(f'{self.url_autorize}/{token}')

        if self.response.status_code == 404:
            # Если токен невалидный, получаем новый
            self.response = requests.post(
                self.url_autorize,
                json=body).json()
            self.json = self.response.json()
            new_token = self.response['token']

            # Перезаписываем файл с новым токеном
            with open(token_data, 'w') as data_file:
                data_file.write(new_token)

            return {'Authorization': new_token}

        elif self.response.status_code == 200:
            # Если токен валидный, используем старый
            self.json = {"token": token}
            return {'Authorization': token}

        else:
            raise Exception(
                f"Unexpected status code: {self.response.status_code}")

    def check_objs_in_auh(self, body):
        if self.json is None:
            raise ValueError(
                "JSON response is None")
        assert ('lyadov' in self.json) == ('lyadov' in body), \
            'Пользователь не найден'
        assert 'token' in self.json, 'token не найдет'
