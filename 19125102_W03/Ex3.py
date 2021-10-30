def munch(a, b):
    def decorator(func):
        def wrapper() :
            assert a < b 
            str_pfib = func()
            x_string = 'x' * (b - a)    
            return str_pfib[:a] + x_string + str_pfib[b:]

        return wrapper

    return decorator

@munch(1, 4)
def decorated_function_with_arguments():
    return "Fibonacci"

print(decorated_function_with_arguments())