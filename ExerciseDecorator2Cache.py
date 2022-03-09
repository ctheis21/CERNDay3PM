import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
    
def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper

@cache
@CountCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)
fibonacci.cache


def power(iterable, nb):
    return [e**nb for e in iterable]

res=power((5,6,7), 3)
print(res, id(res))
res=power((5,6,8,9), 3)
print(res, id(res))
res=power((5,6,7), 3)
print(res, id(res))