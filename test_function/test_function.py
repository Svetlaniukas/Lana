import pytest
import my_function


def test_cinema_movie_name_rating():
    assert my_function.cinema('Alien', 200) == 'Movie: "Alien", rating: 200'
    assert my_function.cinema('Big', 10) == 'Movie: "Big", rating: 10'
    assert my_function.cinema('Booo', 20) == 'Movie: "Booo", rating: 20'
    assert my_function.cinema('', 40) != 'Movie: "Big", rating: 10'


def test_cinema_today():
    assert my_function.cinema_today(
        'Terminator', 30) == 'Movie: "Terminator", rating: 30'
    assert my_function.cinema_today(
        'Hello friend', 200) == 'Movie: "Hello friend", rating: 200'
    assert my_function.cinema_today(
        '', 45) != 'Movie: "Big", rating: 80'


def test_movie_tomorrow():
    assert my_function.cinema_tomorrow(
        'Sunny', 300) == 'Movie: "Sunny", rating: 300'
    assert my_function.cinema_tomorrow(
        'Sunny', 400) != 'Movie: "Sunny", rating: 300'


def test_sum_plius():
    assert my_function.plius(5, 7) == 12
    assert my_function.plius(10, 20) == 30
    assert my_function.plius(10, 20) != 12


def test_sum_minus():
    assert my_function.minus(10, 2) == ('summa:', 8)
    assert my_function.minus(9, 2) != ('summa:', 12)


def test_sum_multiplay():
    assert my_function.multi(10, 5) == ('result:', 50)
    assert my_function.multi(9, 2) != ('result:', 20)
    assert my_function.multi(1, 5) != 'result:', 50


def test_num_divide():
    assert my_function.divide(10, 2) == ('result:', 5)
    assert my_function.divide(20, 2) == ('result:', 10)


def test_staff_book():
    assert my_function.staff_book(
        'Tania', 'Bal', 20
        ) == 'First name:"Tania", Second name:"Bal", Phone numbers:20'

    assert my_function.staff_book(
        'Lena', 'Ross', 34
        ) == 'First name:"Lena", Second name:"Ross", Phone numbers:34'


def Test_string_should_failed():
    with pytest.raises(ZeroDivisionError):
        assert my_function.staff_book("A", "B")
