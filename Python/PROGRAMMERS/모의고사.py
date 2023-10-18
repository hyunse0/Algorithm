def set_len(pattern, goal):
    while len(pattern) < goal:
            pattern *= 2
    
    return pattern


def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    goal = len(answers)
    person1 = set_len(pattern1, goal)
    person2 = set_len(pattern2, goal)
    person3 = set_len(pattern3, goal)

    cnt_lst = []
    for person in (person1, person2, person3):
        cnt = 0
        for i in range(goal):
            if answers[i] == person[i]:
                cnt += 1
        cnt_lst.append(cnt)

    answer = []
    for i in range(3):
        if cnt_lst[i] == max(cnt_lst):
            answer.append(i+1)

    return answer

answers = [1, 2, 3, 4, 5]
print(solution(answers))