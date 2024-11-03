def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

@my_decorator
def say_hello2():
    print("Hello..2!")

say_hello()
say_hello2()