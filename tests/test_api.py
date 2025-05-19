import pytest
import requests


def test_get_meme(authorize):
    response = requests.get(
        'http://167.172.172.115:52355/meme', headers=authorize)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    for meme in data['data']:
        assert 'id' in meme
        assert 'info' in meme
        assert 'tags' in meme
        assert 'text' in meme
        assert 'updated_by' in meme
        assert 'url' in meme


def test_one_meme(crate_meme_id, authorize):
    response = requests.get(
        f'http://167.172.172.115:52355/meme/{crate_meme_id}',
        headers=authorize).json()
    print(response)


def test_put_meme(crate_meme_id, authorize):
    body = {
        "id": crate_meme_id,
        "text": "im driver",
        "url": "https://www.memify.ru/meme/142950/im-driver/",
        "tags": ["driver", "driver2"],
        "info": {"description": "test_info", "color": "pink"}
    }
    response = requests.put(
        f'http://167.172.172.115:52355/meme/{crate_meme_id}',
        headers=authorize,
        json=body).json()
    print(response)


def test_delete_meme(crate_meme_id, authorize):
    response = requests.delete(
        f'http://167.172.172.115:52355/meme/{crate_meme_id}',
        headers=authorize)
    print(response)


