import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Удаление мэма')
    def delete_meme(self, meme_id, authorize):
        self.response = requests.delete(
            f'{self.url}/{meme_id}', headers=authorize)
        try:
            self.json = self.response.json()  # сохраняем JSON в self.json
        except ValueError:
            self.json = None  # если нет JSON
        return self.response  # возвращаем response
