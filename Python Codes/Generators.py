# Generators allow you to iterate over a sequence of values without generating them all at once, saving memory. Generators are created using the yield statement instead of return.
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for num in countdown(5):
    print(num)

# Output:
# 5
# 4
# 3
# 2
# 1

# Explanation:
# Each time `yield` is hit, the function’s state is saved, and the value is returned.
# Execution resumes from the same point in the next iteration.