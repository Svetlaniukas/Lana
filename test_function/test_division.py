import numbers
from os import name

from my_function import (
    greet, greet2, greet3,
    sum_plius, sum_minus, num_multi, num_divide, numeric)


def test_greet():
    assert greet('Alien', 200) == 'Movie: "Alien", rating: 200'


def test_greet2():
    assert greet2('Terminator') == 'Movie: Terminator'


def test_movie():
    assert greet3('Sunny', 300) == 'Sunny 300'


def test_sum():
    assert sum_plius(5, 7) == 12


def test_sum_minus():
    assert sum_minus(10, 2) == ('summa:', 8)


def test_sum_multiplay():
    assert num_multi(10, 5) == ('result:', 50)


def test_num_divide():
    assert num_divide(10, 2) == ('result:', 5)


def test_numeric(sur_name):
    assert numeric({numbers}, {name}, {sur_name}) == (20, 'Tania', 'Bal')

def test_alex(sur_name):
    assert numeric({numbers}, {name}, {sur_name}) == (20, 'alex1, 'Bal1')

