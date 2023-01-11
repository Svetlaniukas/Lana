import json
from typing import Self
from app import app
import pytest

""" Тест должен возвращать текст на главной странице"""
def test_should_return_the_main_page():
    response = app.test_client().get('/')
    assert 'A lot of people ask where we got our name' in response.data.decode(
        'utf-8')


"""Тест должен загружать главную страницу c возвратом текста"""
def test_should_load_the_main_page_with_the_return_text():
    response = app.test_client().get('/home')

    print(response.data)
    assert response.status_code == 200
    assert 'New Look Hair Design' in response.data.decode('utf-8')


"""Тест parametrize  на возврат данных из списка day"""
@pytest.mark.parametrize(
    "day", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    )
def test_to_return_data_from_the_day_list(day):
    response = app.test_client().get('/staff')
    print(f'"{day}"')
    assert 'Monday' in response.data.decode('utf-8')


"""Тест parametrize  на возврат данных из списка weekend"""
@pytest.mark.parametrize("weekend", ['Saturday', 'Sunday'])
def test_to_return_data_from_the_weekend_list(weekend):
    response = app.test_client().get('/staff')
    print(f'"{weekend}"')
    assert 'Sunday' in response.data.decode('utf-8')
    
""" Тест должен возвращать таблицу db на главной странице"""   


def test_should_return_db_table_in_main_page_with_text():
    response = app.test_client().get('/create-article')
    assert 'Apload some text' in response.data.decode('utf-8')
    

@pytest.fixture
def client():
    with app.test_client, self.app_context():
        app.test_client.config['DATABASE'] = True
        app.test_client.config['TESTING'] = True


""" Тест должен возвращать принимать запрос post"""
def test_ishould_return_a_CREATE_button_on_the_main_page():
    with app.test_client, self.app_context():
        data = {
            "user_id": "1",
            "content": "a content",
            "participant1": "participant1",
            "participant2": "participant2",
            "participant3": "participants"
        }

        response = app.test_client.post(
            "/create-article",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(201, response.status_code)
        self.assertEqual(
            'Your message has been successfully saved', response.data)
    
