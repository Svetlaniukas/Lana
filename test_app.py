import pytest

from app import app


def test_index_contain_route():
    response = app.test_client().get('/')
    assert 'A lot of people ask where we got our name' in response.data.decode('utf-8')


def test_index_contain_main_title_name():
    response = app.test_client().get('/home')

    print(response.data)
    assert response.status_code == 200
    assert 'New Look Hair Design' in response.data.decode('utf-8')


def test_index_contain_staff_shift_day():
    response = app.test_client().get('/staff')

    print(response.data)
    assert 'Monday : 10.am-4.pm'
    assert 'Tuesday : 9.am-3.pm'
    assert 'Wednesday : 10.am-5.pm'
    assert 'Thursday : 10am-4pm'
    assert 'Friday : 8am-4pm '
)


