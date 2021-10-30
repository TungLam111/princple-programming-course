def bold(func):
    def wrapper():
        str_return = '<b>{}</b>'.format(func())
        return str_return
    return wrapper

def italics(func):
    def wrapper():
        str_return = '<i>{}</i>'.format(func())
        return str_return
    return wrapper

@bold
@italics
def pfib():
    return 'Fibonacci'

print(pfib())