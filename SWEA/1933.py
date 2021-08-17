N = int(input())

for n in range(1, N+1) :
    if not N%n :
        print(n, end = ' ')