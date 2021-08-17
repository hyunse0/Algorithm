T = int(input())

for t in range(1, T+1) :
    N = int(input())

    result = ''

    for n in range(N) :
        word, cnt = input().split()

        result += word * int(cnt)

    print(f'#{t}')
    for _ in range((len(result)//10) +1) :
        print(result[:10])
        result = result[10 :]