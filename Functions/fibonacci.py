def fibonacci(x):
    if x < 0:
        print("Invalid Input")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


def print_fibonacci_series(terms):
    for i in range(1, terms + 1):
        print(fibonacci(i), end=" ")


# Number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))
print_fibonacci_series(n)


# Optimize method

# def fibonacci_iterative(terms):
#     fib_series = [0, 1]  # Starting two numbers of Fibonacci
#     for i in range(2, terms):
#         next_fib = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_fib)
#     return fib_series

# # Show Fibonacci series for 50 terms
# n = 1000
# fibonacci_series = fibonacci_iterative(n)
# print(fibonacci_series)
