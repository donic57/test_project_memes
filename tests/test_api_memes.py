import allure
import pytest
from endpoints.autorize_meme import Authorize
from endpoints.create_meme import CreateMeme
from data.data_test import DataTest
import requests


@pytest.mark.smoke
@allure.story('Get')
@allure.title('Вызов get запроса со всеми мэмами')
def test_get_memes(get_memes, authorize):
    get_memes.get_all_memes(authorize)
    get_memes.check_status_is_200()
    get_memes.check_data_response()


@pytest.mark.regression
@allure.story('Get')
@allure.title('Вызов get запроса со всеми мэмами и получение статус кода 401')
def test_get_meme_unauthorized(get_memes):
    get_memes.get_all_memes()
    get_memes.check_status_is_401()


@pytest.mark.regression
@allure.story('Get')
@allure.title('Вызов get запроса с одним мэмом по id')
def test_one_meme(get_memes, create_meme, authorize):
    meme_id, meme_body = create_meme
    get_memes.get_one_meme(meme_id, authorize)
    get_memes.check_status_is_200()
    get_memes.check_objs_in_body(meme_id, meme_body)


@pytest.mark.extended
@allure.story('Get')
@allure.title('Вызов get запроса с одним мэмом по id без авторизации')
def test_one_meme_unauthorized(get_memes, create_meme):
    meme_id, _ = create_meme
    get_memes.get_one_meme(meme_id)
    get_memes.check_status_is_401()


@pytest.mark.smoke
@allure.story('Put')
@allure.title('Обновление put запросом по id')
def test_put_meme(put_meme, create_meme, authorize, remove_meme):
    meme_id, _ = create_meme
    body = put_meme.update_body(meme_id)
    put_meme.update_meme(meme_id, body, authorize)
    put_meme.check_status_is_200()
    put_meme.check_objs_in_body(meme_id, body)
    remove_meme.delete_meme(meme_id, authorize)
    remove_meme.check_status_is_200()
    response = put_meme.update_meme(meme_id, body, authorize)
    put_meme.check_noid_status_is_404(response, meme_id)


@pytest.mark.extended
@allure.story('Put')
@allure.title('Обновление put запросом по id без авторизации')
def test_put_meme_unauthorized(put_meme, create_meme):
    meme_id, _ = create_meme
    body = put_meme.update_body(meme_id)
    put_meme.update_meme(meme_id, body)
    put_meme.check_status_is_401()


@pytest.mark.extended
@allure.story('Put')
@allure.title('Обновление put запросом c некорректными данными')
@pytest.mark.parametrize("body", DataTest.TEST_DATA_BAD)
def test_bad_put_meme(put_meme, authorize, body):
    put_meme.bad_update_body(authorize, body)
    put_meme.check_status_is_404()


@pytest.mark.regression
@allure.story('Delete')
@allure.title('Удаление мэма по id')
def test_delete_meme(remove_meme, create_meme, authorize, get_memes):
    meme_id, _ = create_meme
    remove_meme.delete_meme(meme_id, authorize)
    remove_meme.check_status_is_200()
    response = get_memes.get_one_meme(meme_id, authorize)
    remove_meme.check_noid_status_is_404(response, meme_id)


@pytest.mark.extended
@allure.story('Delete')
@allure.title('Удаление мэма по id без авторизации')
def test_delete_meme_unauthorized(remove_meme, create_meme):
    meme_id, _ = create_meme
    remove_meme.delete_meme(meme_id)
    remove_meme.check_status_is_401()


@pytest.mark.regression
@allure.story('Post')
@allure.title('Запуск авторизации и проверка запроса и ответа')
def test_auh():
    auh = Authorize()
    auh.user_authorize()
    auh.check_status_is_200()
    body = {"name": "lyadov"}
    auh.check_objs_in_auh(body)


@pytest.mark.extended
@allure.story('Post')
@allure.title('Неуспешная авторизация с невалидными данными')
def test_auth_failure():
    auh = Authorize()
    invalid_body = {"name": 12345}
    auh.response = requests.post(
        auh.url_autorize, json=invalid_body)
    auh.check_status_is_400()


@pytest.mark.extended
@allure.story('Post')
@allure.title('Создание мэма без авторизации')
def test_create_meme_unauthorized():
    create_meme = CreateMeme()
    result = create_meme.add_meme()
    result.check_status_is_401()


@pytest.mark.extended
@allure.story('Post')
@allure.title('Создание неуспешного мэма с ожидаемым результатом')
@pytest.mark.parametrize("body", DataTest.TEST_DATA)
def test_bad_create_meme(authorize, body):
    meme = CreateMeme()
    result = meme.add_meme(authorize, body, expected_status=False)
    result.check_status_is_400()


@pytest.mark.smoke
@allure.story('Post')
@allure.title('Создание успешного мэма с пустыми строками')
@pytest.mark.parametrize("body", DataTest.TEST_DATA_OK)
def test_create_meme_ok(create_meme_obj, authorize, body):
    create_meme_obj.add_meme(authorize, body)
    obj_id = create_meme_obj.json['id']
    create_meme_obj.check_status_is_200()
    create_meme_obj.check_objs_in_body(obj_id, body)
