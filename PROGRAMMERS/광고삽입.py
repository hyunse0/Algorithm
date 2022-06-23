# 프로그래머스 광고삽입

def solution(play_time, adv_time, logs):

    def str_to_sec(string):
        h, m, s = map(int, string.split(':'))
        return h*3600 + m*60 + s


    def time_format(time):
        if time < 10:
            return '0'+str(time)
        
        return str(time)


    play_time = str_to_sec(play_time)
    adv_time = str_to_sec(adv_time)

    all_time = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = log.split('-')

        start = str_to_sec(start)
        end = str_to_sec(end)

        all_time[start] += 1
        all_time[end] -= 1
    
    for i in range(1, play_time+1):
        all_time[i] += all_time[i-1]
    
    # 구간합을 구하기 위해 누적 값으로 바꾸기
    # [0, 1, 2, 2, 1] 에서 1~4초 구간합은 1(1~2초)+2(2~3초)+2(3~4초) = 5인데 
    # 누적 값으로 바꾸면 일일이 더하지 않고 인덱싱의 차로 구할 수 있음
    # [0, 1, 3, 5, 6] 에서 1~4초 구간합은 리스트[3](0~3초) - 리스트[0](0~1초) = 5
    for i in range(1, play_time+1):
        all_time[i] += all_time[i-1]
    
    max_cnt = 0
    max_time = 0
    for t in range(play_time-adv_time+1):
        if t:
            cnt = all_time[t+adv_time-1] - all_time[t-1]
        else:
            cnt = all_time[t+adv_time-1]
        
        if max_cnt < cnt:
            max_cnt = cnt
            max_time = t

    h, max_time = divmod(max_time, 3600)
    m, s = divmod(max_time, 60)

    return time_format(h) + ':' + time_format(m) + ':' + time_format(s)


logs = ["00:00:02-00:00:06", "00:00:03-00:00:04", "00:00:04-00:00:07", "00:00:04-00:00:06", "00:00:05-00:00:07"]
print(solution("00:00:08", "00:00:03", logs))