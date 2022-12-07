import pytest
from datetime import datetime, timedelta
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


testdata = [
    (datetime(2023, 12, 12), datetime(2023, 12, 11), timedelta(1)),
    (datetime(2023, 12, 11), datetime(2023, 12, 12), timedelta(-1)),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected


def idfn(val):
    if isinstance(val, (datetime,)):
        # note this wouldn't show any hours/minutes/seconds
        return val.strftime("%Y%m%d")


@pytest.mark.parametrize("a,b,expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        pytest.param(
            datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1), id="forward"
        ),
        pytest.param(
            datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1), id="backward"
        ),
    ],
)
def test_timedistance_v3(a, b, expected):
    diff = a - b
    assert diff == expected

