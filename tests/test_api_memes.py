import allure
import pytest
from endpoints.update_meme import UpdateMeme


@allure.story('Get')
@allure.title('Вызов get запроса со всеми мэмами')
def test_get_meme(get_memes, authorize):
    get_memes.get_all_memes(authorize)
    get_memes.check_status_is_200()
    get_memes.check_data_response()


@allure.story('Get')
@allure.title('Вызов get запроса со всеми мэмами и получение статус кода 401')
def test_get_meme_unauthorized(get_memes):
    get_memes.get_memes_unauthorized()
    get_memes.check_status_is_401()


@allure.story('Get')
@allure.title('Вызов get запроса с одним мэмом по id')
def test_one_meme(get_memes, create_meme, authorize):
    meme_id, meme_body = create_meme
    get_memes.get_one_meme(meme_id, authorize)
    get_memes.check_status_is_200()
    get_memes.check_objs_in_body(meme_body)


@allure.story('Put')
@allure.title('Обновление put запросом по id')
def test_put_meme(put_meme, create_meme, authorize):
    meme_id, _ = create_meme
    body = put_meme.update_body(meme_id)
    put_meme.update_meme(meme_id, authorize, body)
    put_meme.check_status_is_200()
    put_meme.check_objs_in_body(body)


@allure.story('Put')
@allure.title('Обновление put запросом c некорректными данными')
@pytest.mark.parametrize("body", UpdateMeme.TEST_DATA)
def test_bad_put_meme(put_meme, authorize, body):
    put_meme.bad_update_body(authorize, body)
    put_meme.check_status_is_400()


@allure.story('Delete')
@allure.title('Удаление мэма по id')
def test_delete_meme(remove_meme, create_meme, authorize):
    meme_id, _ = create_meme
    remove_meme.delete_meme(meme_id, authorize)
    remove_meme.check_status_is_200()
