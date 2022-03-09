import math

class desc:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if self.name=="area":
            return math.pi * instance.radius ** 2
        elif self.name=="perimeter":
            return 2 * math.pi * instance.radius
        else:
            raise AttributeError(f"{self.name} is not an attribute")
    def __set__(self, instance, value):
        raise AttributeError(f"{self.name} is a readOnly attribute")


class Circle:
    area=desc("area")
    perimeter=desc("perimeter")
    
    def __init__(self, radius):
        self.radius = radius

c=Circle(10)
print(c.radius)
print(c.area)
print(c.perimeter)
c.radius=20
print(c.radius)
print(c.area)
print(c.perimeter)
c.area=100