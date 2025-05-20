import pytest
import requests
from endpoints.delete_meme import DeleteMeme
from endpoints.getting_memes import GettingMemes
from endpoints.update_meme import UpdateMeme
import os


@pytest.fixture(scope='session')
def authorize():
    base_way = os.path.dirname(__file__)
    token_file_way = os.path.dirname(base_way)
    token_data = os.path.join(
        token_file_way, 'test_project_memes', 'tests', 'token_file')
    body = {"name": "lyadov"}

    # Читаем текущий токен из файла
    with open(token_data, 'r') as data_file:
        token = data_file.readline().strip()

    # Проверяем токен
    response = requests.get(f"http://167.172.172.115:52355/authorize/{token}")

    if response.status_code == 404:
        # Если токен невалидный, получаем новый
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=body
        ).json()
        new_token = response['token']

        # Перезаписываем файл с новым токеном
        with open(token_data, 'w') as data_file:
            data_file.write(new_token)

        return {'Authorization': new_token}

    elif response.status_code == 200:
        # Если токен валидный, используем старый
        return {'Authorization': token}

    else:
        raise Exception(f"Unexpected status code: {response.status_code}")


@pytest.fixture()
def create_meme(authorize):
    body = {
        "text": "Спасибо всем народам, которые дружат за 3 выходных",
        "url": "https://www.memify.ru/meme/128787/",
        "tags": ["kotey", "andrey"],
        "info": {"description": "test_info"}
    }
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        headers=authorize,
        json=body).json()
    return response['id'], body


@pytest.fixture()
def get_memes():
    return GettingMemes()


@pytest.fixture()
def put_meme():
    return UpdateMeme()


@pytest.fixture()
def remove_meme():
    return DeleteMeme()
