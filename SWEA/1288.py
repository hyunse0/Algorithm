T = int(input())
i = 0

for _ in range(T) :
    N = int(input())

    check_list = [0 for x in range(10)]
    
    n = 1

    while True :
        new_N = N * n

        while new_N :
            check_list[new_N%10] += 1
            new_N //= 10


        if 0 not in check_list :
            break
        else : 
            n += 1

    i += 1
    print(f'#{i} {N*n}')