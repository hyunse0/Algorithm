def solution(n, lost, reserve):
    lost_len = len(lost)
    cnt = [0]*lost_len

    for i in range(lost_len):
        if lost[i]+1 in reserve:
            cnt[i] += 1

        if lost[i]-1 in reserve:
            cnt[i] += 1

    if sum(cnt) == 2*lost_len:
        return n
    elif sum(cnt) == 0:
        return n-lost_len

    for j in range(lost_len):
        if cnt[j] == 1:
            cnt[j] -=1
            lost.remove(lost[i])




    answer = 0

    return answer