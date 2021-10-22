def solution(n,a,b):
    team = [x for x in range(n+1)]
    rank = [0 for _ in range(n+1)]

    jump = 2
    answer = 0
    while True:
        if team[a] == team[b]:
            return answer
        else:
            answer += 1

            for i in range(1, n, jump):
                leader_x = team[i]
                leader_y = team[i+jump//2]

                if rank[leader_x] >= rank[leader_y]:
                    for i in range(n+1):
                        if team[i] == leader_y:
                            team[i] = leader_x
                    if rank[leader_x] == rank[leader_y]:
                        rank[leader_x] += 1
                else:
                    for i in range(n+1):
                        if team[i] == leader_x:
                            team[i] = leader_y
            
            jump *= 2

print(solution(8, 4, 7))