def my_deco(func):
    def wrapper():
        print('+----------+')
        print('|          |')
        print(' ',func(),' ')
        print('|          |')
        print('+----------+')
    return wrapper

@my_deco
def pfib():
    return 'Fibonacci'


pfib()