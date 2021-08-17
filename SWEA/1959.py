T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N >= M :
        max_num = 0

        for _ in range(N - M + 1) :
            total = 0

            for a, b in list(zip(A, B)) :
                total += (a*b)
            
            if total > max_num :
                max_num = total
            
            B.insert(0, 0)
    else :
        max_num = 0

        for _ in range(M - N + 1) :
            total = 0

            for a, b in list(zip(A, B)) :
                total += (a*b)
            
            if total > max_num :
                max_num = total
            
            A.insert(0, 0)

    print(f'#{t} {max_num}')