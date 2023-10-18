T = int(input())

for t in range(1, T+1):
    N = int(input())
    farm = []

    for _ in range(N):
        farm.append(input())
    
    i = N//2
    k = 1
    result = 0
    flag = True

    for row in farm:
        if k > N:
            flag = False
            i += 2
            k -= 4

        for num in row[i:i+k]:
            result += int(num)

        if flag:
            i -= 1
            k += 2
        else:
            i += 1
            k -= 2
    
    print('#{} {}'.format(t, result))