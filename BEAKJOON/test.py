T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [x for x in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            apart[i] += apart[i-1]
    
    print(apart[-1])