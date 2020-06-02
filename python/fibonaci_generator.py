def fibonacci(limit):
    # Generators use 'yield' to create an iterator.  This one allows the caller to 
    # get the Fibonacci sequence using an iterator
    a, b = 0, 1

    while a < limit:
        # Return the current value of 'a'
        yield a
        # Update a and b
        a, b = b, a+b

if __name__ == "__main__":
    for i in fibonacci(8):
        print(i)
