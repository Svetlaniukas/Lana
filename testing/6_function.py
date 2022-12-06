from multiprocessing import context

movie = 'Alien'
rating = 200
result = f'Movie: "{movie}", rating: {rating}'
print(result)

result = f'Movie: "{movie}", rating: {rating}'
print(result)


def greet2():
    result2 = f'Movie: {movie}'
    print(result2)

greet2()


def greet3(movie='good_day', rating=300, ):
    result1 = f'{movie}, {rating}'
    print(result1)

greet3()
greet3('Alien3', 100)
greet3('Terminator', 34)



def sum(first, second):
    result = first + second
    print(result)

sum(5, 7)
sum(2, 2)

def sum_minus(first, second):
    result = first - second
    print(result)

sum_1 = ('summa:', sum_minus(10, 2))




def num_multiplay(first, second):
    result = first * second
    print(result)


num_2 = ('result:', num_multiplay(10, 5))


def num_divide(first, second):
    result = first / second
    print(result)


num_3 = ('result:', num_divide(10, 2))



def numeric(id=1, name='Lana', surname='Mel'):
    context = f'{id}, {name}, {surname}'
    print(context)

numeric()
numeric(12, 'Alex', 'Melix')
print(context)
numeric = (30, 50, 3)
print(numeric)
num = (50 - 20 - 3)
print(num)
num1 = ('result:', 10 * 5)
print(num1)
staff = ('result:', 35 - 10)
print(staff)
num3 =('result:', 20 / 2)
print(num3)


