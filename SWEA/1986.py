T = int(input())

for t in range(1, T+1):
    N = int(input())

    total = 0
    for n in range(1, N+1):
        if n%2:
            total += n
        else:
            total -= n
    
    print('#{} {}'.format(t, total))