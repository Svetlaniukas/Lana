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


def staff_book(name, surname, telephone):
    result = f'First name:"{name}", Second name:"{surname}", Phone numbers:{telephone}'
    print(result, int(telephone))
    return result


def sum_not_exist():
    result =(a + b) + 12
    print(result)
    return result

