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
sum('summa:', str(10 - 2))
print()
sum('all is good', str(123))
print()
sum(int(10), int(-5))
print()
sum('result:', str(10 * 5))
print()
sum('result:', str(10 / 2))
print()






