import pytest

import my_function


def test_cinema_mane_rating():
    assert my_function.cinema('Alien', 200) == 'Movie: "Alien", rating: 200'
    assert my_function.cinema('Big', 10) == 'Movie: "Big", rating: 10'
    assert my_function.cinema('Big', '') == 'Movie: "Big", rating: 10'
    assert my_function.cinema('Big', 40) != 'Movie: "Big", rating: 10'


def test_cinema_today():
    assert my_function.cinema_today('Terminator', 30) == 'Movie: "Terminator", rating: 30'
    assert my_function.cinema_today('') == 'Movie: "Alien"'
    assert my_function.cinema_today('Big', 45) != 'Movie: "Big"'


def test_movie_tomorrow():
    assert my_function.cinema_tomorrow('Sunny', 300) == 'Movie: "Sunny", rating: 300'
    assert my_function.cinema_tomorrow('Sunny', 400) != 'Movie: "Sunny", rating: 300'


def test_sum():
    assert my_function.plius(5, 7) == 12
    assert my_function.plius(5, 7) == 30
    assert my_function.plius(10,20) != 12


def test_sum_minus():
    assert my_function.minus(10, 2) == 'summa:', 8
    assert my_function.minus(13, 2) != 'summa:', 8

def test_sum_multiplay():
    assert my_function.multi(10, 5) == 'result:', 50
    assert my_function.multi(9,0) == 'result:', 80
    assert my_function.multi(1, 5) != 'result:', 50

def test_myfunc_should_be_faled():
    with pytest.raises(ValueError):
    assert sum_not_exist(4,7)


def test_num_divide():
    assert my_function.divide(10, 2) == ('result:', 5)
    assert my_function.divide(20, 2) == ('result:', 10)



def test_sum_not_exist():
    with pytest.raises(ValueError):
        assert my_function.sum_not_exist()


def test_staff_book(doctest_namespace):
    assert my_function.staff_id({}, {}, {}) == 'name: "Tania", surname: "Bal", rating: 20'
