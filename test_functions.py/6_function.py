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



def sum(first='numeric', second=33):
    result = first + second
    print(result)

sum(5, 7)
sum1 = ('summa:', 10 - 2)
print(sum1)
sum2 = ('all is good', 123)
print(sum2)
sum3 = ('summa:', 25 - 5)
print()
sum4 = ('result:', str(10 * 5))
print()
sum5 = ('result:', str(10 / 2))
print()


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





