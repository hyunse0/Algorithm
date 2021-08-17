T = int(input())

for t in range(1, T+1) :
    N = input()
    print(N)

    check_list = [0 for x in range(10)]
    
    n = 1

    while True :
        new_N = str(int(N) * n)
        print(new_N)

        for num in new_N :
            check_list[int(num)] += 1

        if 0 not in check_list :
            break
        else : 
            n += 1

    print(f'#{t} {new_N}')