import requests
import allure
from endpoints.endpoint import Endpoint


class GettingMemes(Endpoint):

    @allure.step('Вызов get запроса со всеми объектами')
    def get_all_memes(self, authorize=None):
        if authorize is None:
            self.response = requests.get(self.url)
        else:
            self.response = requests.get(self.url, headers=authorize)
        try:
            self.json = self.response.json()  # сохраняем JSON в self.json
        except ValueError:
            self.json = None  # если нет JSON
        return self.response  # возвращаем response

    @allure.step('Проверка наличия всех полей в ответе')
    def check_data_response(self):
        assert 'data' in self.json
        for meme in self.json['data']:
            assert 'id' in meme
            f"Object missing 'id' field: {meme}"
            assert 'info' in meme
            f"Object missing 'id' field: {meme}"
            assert 'tags' in meme
            f"Object missing 'id' field: {meme}"
            assert 'text' in meme
            f"Object missing 'id' field: {meme}"
            assert 'updated_by' in meme
            f"Object missing 'id' field: {meme}"
            assert 'url' in meme
            f"Object missing 'id' field: {meme}"

    @allure.step('Вызов get запроса по id')
    def get_one_meme(self, meme_id, authorize=None):
        if authorize is None:
            self.response = requests.get(
                f'{self.url}/{meme_id}')
        else:
            self.response = requests.get(
                f'{self.url}/{meme_id}', headers=authorize)
        try:
            self.json = self.response.json()  # сохраняем JSON в self.json
        except ValueError:
            self.json = None  # если нет JSON
        return self.response  # возвращаем response
