T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())

    people = list(map(int, input().split()))
    people.sort() # 시간 순으로 정렬

    time = people[-1]
    bread = 0
    person = 0
    i = 0

    result = 'Possible'
    for sec in range(time+1):
        # 초가 M으로 나누어 떨어지면 붕어빵 K개 추가(0초에는 x)
        if sec and not sec % M:
            bread += K
        
        # people에 명시된 초가 되면 사람이 한 명 늘고 people의 다음 인덱스 가리킴
        if people[i] == sec:
            while i < N and people[i] ==sec:
                person += 1
                i += 1
        
        # 만약, 1초라도 붕어빵보다 사람이 많으면 기다리게 됨 -> 불가능
        if person > bread:
            result = 'Impossible'
            break

    print('#{} {}'.format(t, result))