
#------------ with ------------
# with open("file.txt", "r") as file:
#     data = file.read()
#------------------------------



# A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. Common examples of higher-order functions include map, filter, reduce, and custom implementations that accept functions as parameters.
# A higher-order function that applies a given function to all items in a list
def apply_function(func, numbers):
    return [func(n) for n in numbers]

# A function that doubles a number
def double(x):
    return x * 2

# A function that squares a number
def square(x):
    return x ** 2

# Using the higher-order function
numbers = [1, 2, 3, 4, 5]
print(apply_function(double, numbers))  # Output: [2, 4, 6, 8, 10]
print(apply_function(square, numbers))  # Output: [1, 4, 9, 16, 25]
