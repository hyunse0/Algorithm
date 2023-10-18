


T = int(input())

for t in range(1, T+1) :
    N = int(input())

    result = []

    while N != 1 :
        if not N%2 :
            result.append(2)
            N /= 2
        elif not N%3 :
            result.append(3)
            N /= 3
        elif not N%5 :
            result.append(5)
            N /= 5
        elif not N%7 :
            result.append(7)
            N /= 7
        elif not N%11 :
            result.append(11)
            N /= 11

    print(f'#{t}', end = ' ')

    for a in [2, 3, 5, 7, 11] :
        if a == 11 :
            print(f'{result.count(a)}')
        else :
            print(f'{result.count(a)}', end = ' ')
