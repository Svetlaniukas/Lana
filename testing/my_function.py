def cinema(actor, stars):
    result = f'Movie: "{actor}", rating: {stars}'
    print(result)
    return result


def cinema_tomorrow(movie, rating):
    result = f'Movie: "{movie}", rating: {rating}'
    print(result)
    return result


def cinema_today(movie, rating):
    result = f'Movie: "{movie}", rating: {rating}'
    print(result)
    return result


def staff_id(actor, surname, stars):
    result = f'name: "{actor}", surname: {surname}, rating: {stars}'
    print(result)
    return result


def plius(a, b):
    result = int(a + b)
    print(result)
    return result


def minus(b, c):
    result = f'summa:', int(b - c)
    print(result)
    return result


def multi(a, c):
    result = f'result:', int(a * c)
    print(result)
    return result


def divide(a, b):
    result = f'result:', int(a / b)
    print(result)
    return result


def sum_not_exist():
    a = 'hello'
    b = - 4
    print(a, b)
    return a, b

