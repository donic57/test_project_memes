import pytest
import requests
from endpoints.delete_meme import DeleteMeme
from endpoints.getting_memes import GettingMemes
from endpoints.update_meme import UpdateMeme


@pytest.fixture(scope='session')
def authorize():
    body = {
        "name": "lyadov"
    }
    response = requests.post(
        'http://167.172.172.115:52355/authorize', json=body).json()
    return {'Authorization': response['token']}


@pytest.fixture()
def crate_meme(authorize):
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
def crate_meme_id(authorize):
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
    return response['id']


@pytest.fixture()
def get_memes():
    return GettingMemes()


@pytest.fixture()
def put_meme():
    return UpdateMeme()


@pytest.fixture()
def remove_meme():
    return DeleteMeme()