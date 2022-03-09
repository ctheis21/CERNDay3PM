import atexit

@atexit.register
def f1():
    print("I'm function f1")

@atexit.register    
def f2():
    print("I'm function f2")
    

d=[5,7,8]
print(d)
print("The end")

