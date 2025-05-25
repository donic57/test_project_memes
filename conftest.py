import pytest
from endpoints.delete_meme import DeleteMeme
from endpoints.getting_memes import GettingMemes
from endpoints.update_meme import UpdateMeme
from endpoints.autorize_meme import Authorize
from endpoints.create_meme import CreateMeme


@pytest.fixture(scope='session')
def authorize():
    auh = Authorize()
    return auh.user_authorize()


@pytest.fixture()
def create_meme(authorize):
    meme = CreateMeme()
    result = meme.add_meme(authorize)
    meme_id = result.json['id']
    meme_body = result.json
    yield meme_id, meme_body
    # После теста удаляем мем
    DeleteMeme().delete_meme(meme_id, authorize)


@pytest.fixture()
def get_memes():
    return GettingMemes()


@pytest.fixture()
def put_meme():
    return UpdateMeme()


@pytest.fixture()
def remove_meme():
    return DeleteMeme()
