T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    score = []
    for i in range(1, N+1):
        a, b, c = map(int, input().split())
        temp = a*0.35 + b*0.45 + c*0.2

        if i == K:
            target = temp

        score.append(temp)
    
    score.sort(reverse=True)
    rank = score.index(target)+1
    grade = rank/N*100

    if grade <= 10:
        result = 'A+'
    elif grade <= 20:
        result = 'A0'
    elif grade <= 30:
        result = 'A-'
    elif grade <= 40:
        result = 'B+'
    elif grade <= 50:
        result = 'B0'
    elif grade <= 60:
        result = 'B-'
    elif grade <= 70:
        result = 'C+'
    elif grade <= 80:
        result = 'C0'
    elif grade <= 90:
        result = 'C-'
    else:
        result = 'D0'

    print('#{} {}'.format(t, result))
    