from typing import Tuple
from unicodedata import name
from unittest import result

import first


def greet(movie, rating):
    result = f'Movie: "{movie}", rating: {rating}'
    print(result)
    return result


greet('Alien', 200)


def greet2(movie):
    result2 = f'Movie: {movie}'
    print(result2)
    return result2


greet2('Terminator')


def greet3(movie, rating):
    result1 = f'{movie} {rating}'
    print(result1)
    return result1


greet3("Sunny", 300)


def sum_plius(first, second):
    result3 = first + second
    print(result3)
    return result3


sum_plius(5, 7)
sum_plius(2, 2)


def sum_minus(first, second):
    result4 = f'summa:', int(first - second)
    print(result4)
    return result4


sum_minus(10, 2)


def num_multi(first, second):
    result5 = f'result:', int(first * second)
    print(result5)
    return result5


num_multi(10, 5)


def num_divide(first, second):
    result6 = f'result:', int(first / second)
    print(result6)
    return result6


num_divide(10, 2)


def numeric(numbers=20, name='Tania', sur_name='Bal'):
    result7 = f'{numbers}, {name}, {sur_name}'
    print(result7)
    return result7

numeric()
