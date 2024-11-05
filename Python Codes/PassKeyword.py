# The pass statement in Python is a placeholder that does nothing when executed. It’s often used as a placeholder in code where a statement is syntactically required but where no action is necessary, allowing you to define a structure or outline your code without implementing functionality right away.
#------------------------------------
def process_data(data):
    pass  # To be implemented later

# Calling the function won't cause an error, but it does nothing
process_data("sample_data")

#------------------------------------
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        pass  # Placeholder for even numbers
    else:
        print(num)  # Only odd numbers will be printed

#------------------------------------
class MyClass:
    pass

# Creating an instance of the empty class
obj = MyClass()