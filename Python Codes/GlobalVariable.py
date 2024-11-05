# Global variable
count = 0

def increment():
    global count  # Declare that we are using the global variable 'count'
    count += 1
    print(f"Count after incrementing: {count}")

def reset():
    # global count # --- if we comment this then it will use it as local variable.
    count = 0
    print("Count reset to 0")

# Using the functions
increment()  # Output: Count after incrementing: 1
increment()  # Output: Count after incrementing: 2
reset()      # Output: Count reset to 0
increment()  # Output: Count after incrementing: 1