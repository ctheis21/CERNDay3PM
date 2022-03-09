class Celsius:
    def __get__(self, instance, owner):
        print(instance, owner)
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5


class Temperature:

    celsius = Celsius()
    
    def __init__(self, initial_f):
        self.fahrenheit = initial_f
    def __repr__(self):
        return f"Temperature is {self.fahrenheit}F ({self.celsius}C)"


t = Temperature(212)
Temperature.celsius
print(t.celsius)
print(t)
t.celsius = 0
print(t.fahrenheit)
print(t.__dict__)