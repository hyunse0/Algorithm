def factorial(n):
    if n == 0:
        return 1
    elif n < 3:
        return n
    else:
        return n*factorial(n-1)

N = int(input())
print(factorial(N))