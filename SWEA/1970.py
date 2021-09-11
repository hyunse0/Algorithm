T = int(input())

for t in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []

    for m in money:
        result.append(N // m)
        N %= m

    print('#{}'.format(t))
    print(*result)

