movie = 'Alien'
rating = 200
result = f'Movie: "{movie}", rating: {rating}'
print(result)

result = f'Movie: "{movie}", rating: {rating}'
print(result)


def greet2():
    """
    :param movie:
    """
    result2 = f'Movie: {movie}'
    print(result2)

greet2()


def greet3(movie='good_day', rating=300, ):
    """

    :param movie:
    :param rating:
    """
    result3 = f'City:{movie}, {rating}'
    print(result3)

greet3()


def greet4(massage='world', name='oleg'):
    """

    :param massage:
    :param name:
    """
    result4 = f'Movie: {massage}, {name}'
    print(result4)

greet4()




def greet5(massage='Hello'):
    """

    :param massage:
    """
    result5 = f'massage{massage}'
    print(result5)

greet5()


def greet6(massage='Hello', name='asdf'):
    """

    :param massage:
    :param name:
    """
    result6 = f'{massage}, {name}'
    print(result6)

greet6()


# greet ( name= 'asdf', 'Hello')


# greeting = 'Hello'
# token = 'world'

def greet7(name='greeting', massage='to'):
    """

    :param name:
    :param massage:
    """
    result7 = f' {name} {massage}, '
    print(result7)

greet7()


# greet (greeting , to)

# massage = greeting = 'hello'

def greet8(name='greeting', massage='to'):
    """

    :param name:
    :param massage:
    :return:
    """
    g = f'str{massage}, {name}'
    return (g)

greet8()


# g = greet(greeting, to)
# print(g)

def greet9(name='hello'):
    """
    :param name:
    """
    g = f'greet{name}'
    print(g)

greet9()


