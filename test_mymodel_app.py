import pytest
from app import app


def test_index_contain_route():
    response = app.test_client().get('/')
    assert 'A lot of people ask where we got our name' in response.data.decode(
        'utf-8')


def test_index_contain_main_title_name():
    response = app.test_client().get('/home')

    print(response.data)
    assert response.status_code == 200
    assert 'New Look Hair Design' in response.data.decode('utf-8')


@pytest.mark.parametrize(
    "day", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    )
def test_index_contain_staff_shift_week_day(day):
    response = app.test_client().get('/staff')
    print(f'"{day}"')
    assert 'Monday' in response.data.decode('utf-8')


@pytest.mark.parametrize("weekend", ['Saturday', 'Sunday'])
def test_index_contain_staff_shift_weekend(weekend):
    response = app.test_client().get('/staff')
    print(f'"{weekend}"')
    assert 'Sunday' in response.data.decode('utf-8')
