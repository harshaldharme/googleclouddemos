# A closure is a function that “remembers” the environment in which it was created, even if it’s called outside that environment. Closures are useful for creating functions with “private” data.
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

# Create a closure
my_closure = outer_function("Hello, World!")
my_closure()  # Output: Hello, World!

# Explanation:
# `inner_function` has access to `message`, a variable defined in `outer_function`.
# When `outer_function` returns `inner_function`, it retains access to `message`.