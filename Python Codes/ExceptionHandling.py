# Exception handling in Python allows a program to handle errors gracefully without crashing. The try block is used to write code that might throw an exception, except to handle exceptions, else for code that should run if no exception occurs, and finally for code that should always run.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division was successful.")
finally:
    print("Execution completed.")
# Output:
# Cannot divide by zero!
# Execution completed.