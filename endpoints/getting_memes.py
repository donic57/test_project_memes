import requests
import allure
from endpoints.endpoint import Endpoint


class GettingMemes(Endpoint):

    @allure.step('Вызов get запроса со всеми объектами')
    def get_all_memes(self, authorize):
        self.response = requests.get(self.url, headers=authorize)
        self.json = self.response.json()
        return self.response

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
    def get_one_meme(self, meme_id, authorize):
        self.response = requests.get(f'{self.url}/{meme_id}', headers=authorize)
        self.json = self.response.json()
        return self.json
