class Person:
    def __init__(self, name, age):
        self.name = name   # Assigns the name attribute to the instance
        self.age = age     # Assigns the age attribute to the instance

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.greet())