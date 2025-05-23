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
    # получаем генератор
    generator = meme.add_meme(authorize)
    # получаем первые значения из генератора
    meme_id, meme_body = next(generator)
    # возвращаем значения тесту
    yield meme_id, meme_body
    try:
        # завершаем работу генератора (выполнится finally-блок в add_meme)
        next(generator)
    except StopIteration:
        pass


@pytest.fixture()
def get_memes():
    return GettingMemes()


@pytest.fixture()
def put_meme():
    return UpdateMeme()


@pytest.fixture()
def remove_meme():
    return DeleteMeme()
