import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Удаление мэма')
    def delete_meme(self, crate_meme_id, authorize):
        self.response = requests.delete(
            f'{self.url}/{crate_meme_id}', headers=authorize)
        return self.response