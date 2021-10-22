def solution(n,a,b):
    people = [x for x in range(n+1)]

    answer = 1
    while True:
        winner = [0]
        for i in range(1, len(people), 2):
            if people[i] == a and people[i+1] == b:
                return answer
            elif people[i] != a and people[i] != b:
                winner.append(people[i+1])
            else:
                winner.append(people[i])

        answer += 1
        people = winner

print(solution(8, 4, 7))