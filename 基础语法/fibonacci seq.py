def fibonacci_seq(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)
print(fibonacci_seq(24))