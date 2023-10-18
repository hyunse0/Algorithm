T = int(input())

for _ in range(T) :
    i = int(input())
    scores = list(map(int, input().split()))

    max_cnt = 0

    for score in set(scores) :
        if scores.count(score) > max_cnt :
            max_cnt = scores.count(score)

    max_cnt_list = []

    for score in set(scores) :
        if scores.count(score) == max_cnt :
            max_cnt_list.append(score)

    print(f'#{i} {max(max_cnt_list)}')