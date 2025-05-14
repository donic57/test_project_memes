import pytest
import requests

@pytest.fixture(scope='session')
def authorize():
    body = {
        "name": "lyadov"
    }
    response = requests.post(
        'http://167.172.172.115:52355/authorize', json=body).json()
    return {'Authorization': response['token']}


def test_get_meme(authorize):
    response = requests.get(
        'http://167.172.172.115:52355/meme', headers=authorize).json()
    print(response)

