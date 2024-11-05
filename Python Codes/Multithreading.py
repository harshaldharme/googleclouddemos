# Multithreading allows you to run multiple threads (smaller units of a process) concurrently, which can help improve performance for I/O-bound tasks like network requests. Python’s Global Interpreter Lock (GIL) limits true parallelism for CPU-bound tasks, but multithreading can still be useful for I/O-bound tasks.
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in "abcde":
        print(f"Letter: {letter}")
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for both threads to finish
thread1.join()
thread2.join()

# Output (order may vary because of concurrent execution):
# Number: 0
# Letter: a
# Number: 1
# Letter: b
# Number: 2
# Letter: c
# Number: 3
# Letter: d
# Number: 4
# Letter: e