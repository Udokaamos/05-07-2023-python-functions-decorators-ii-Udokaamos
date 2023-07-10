from os import system as x
# Solution 1
def validate_numeric(func):
    """This function validate_numeric to validate if the input arguments
    of a function are numeric (types int or float).
    If any of the arguments passed to the function are not numeric, it should return a message The input arguments must be numeric and stop execution. 
    Otherwise, it should execute the decorated function normally
    """
    def wrapper(a, b):
        if type(a) == int and type(b) == int:
            result = func(a,b)
            return result 
        elif type(a) == int and type(b) == float:
            result = func(a, b)
            return result
        elif type(a) == float and type(b) == int:
            result = func(a,b)
            return result
        else:
            return f'The input arguments must be numeric'
    return wrapper


@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))

input()
x("clear")
# Solution 2
def debug(func):
    """This decorator simply outputs the information about the input and output arguments. 
    It indicates both the positional and keyword arguments passed to the function 
    and the output before returning it.
    """
    def wrapper(*args, **kwargs):
        print('**********')
        if args:
            now = format(",".join([str(arg)for arg in args]))
            print(f'Positional arguments: {now}')
        else:
            print('There are no positional arguments')     
        if kwargs:  
            print('Keyword aguments:{}'. format(",".join([f'{s}={t}'for s,t in kwargs.items()])))   
        else:
            print('There are no keyword arguments')       
        result = func(*args, **kwargs)
        print(f'Result: {result}')
    return wrapper

@debug
@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

sum(1, 2)
sum(a=1, b=2)
sum(1, "a")

input()
x("clear")
# Solution 3
def cache(func):
    """This decorator stores in memory the output of every particular call to a function.
    If we call the function twice with the same input parameters, the function will not be called 
    the second time and the result will be fetched from the cache instead.
    """
    memory = dict()
    def wrapper(*args):
        if func.__name__ in memory:
            if memory[func.__name__].get(args):
                return f"Using the cache\n{memory[func.__name__].get(args)}"
        newResult = {
            func.__name__: {
                (args): func(*args)
            }
        }
        memory.update(newResult)
        return f'calculating\n{func(*args)}'
    return wrapper

@cache
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))