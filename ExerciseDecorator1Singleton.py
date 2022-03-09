import functools
from dataclasses import dataclass

def singleton(cls):
    """
    Make a class a Singleton class 
    (only one instance of it can be created)
    """
    @functools.wraps(cls)
    def wrapper_sing(*args, **kwargs):
        if not wrapper_sing.instance:
            wrapper_sing.instance = cls(*args, **kwargs)
        return wrapper_sing.instance
    wrapper_sing.instance = None
    return wrapper_sing

@singleton
class TheOne:
    pass

print(type(TheOne))
first_one = TheOne()
another_one = TheOne()
print(id(first_one))
print(id(another_one))
print(first_one is another_one)


@singleton
@dataclass
class UniquePoint:
    x:int=0
    y:int=0
    
p=UniquePoint(2,3)
print(p, id(p))

p2=UniquePoint(12,4)
print(p, id(p))