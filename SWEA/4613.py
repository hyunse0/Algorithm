T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []

    for _ in range(N):
        color = input()
        temp = []

        for c in color:
            temp.append(c)

        arr.append(temp)

    # 맨 위/아래를 제외한 행 중에서 B가 가장 많이 들어있는 행을 찾기
    max_cnt_B = 0
    for row in arr[1:N-1]:
        if row.count('B') > max_cnt_B:
            max_cnt_B = row.count('B')

    max_B = []
    for i in range(1, N-1):
        if arr[i].count('B') == max_cnt_B:
    
            max_B.append(i)
    # B가 가장 많이 들어있는 행이 여러개라면?
    if len(max_B) > 1:
        pass
    # B가 가장 많이 들어있는 행이 0개라면?
    elif not len(max_B):
        pass
    # 1개
    else:
        pass