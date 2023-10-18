import sys

T = int(sys.stdin.readline())

for t in range(1, T+1):
    string = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    # 문자마다 문자열에 몇 개가 들어있는지 저장
    str_cnt = {}
    for s in string:
        if s in str_cnt.keys():
            str_cnt[s] += 1
        else:
            str_cnt[s] = 1
    
    # K개 이상 있는 문자만 따로 저장
    keys = []
    for key, value in str_cnt.items():
        if value >= K:
            keys.append(key)
    
    # K개 이상 있는 문자가 없다면 -1 출력
    if not keys:
        print(-1)
    
    # K개 이상 있는 문자에 대해 문자열 게임 진행
    else:
        min_str = 10000
        max_str = 0

        for i in range(len(string)):
            # 시작하는 문자 포함해서 카운팅 -> 1
            cnt = 1

            if string[i] in keys:
                for j in range(i+1, len(string)):
                    if string[j] == string[i]:
                        cnt += 1

                    if cnt == K:
                        break
                
                # cnt가 1이면 해당 문자 뒤에 똑같은 문자를 찾지 못한것
                if cnt == 1:
                    break

                len_str = j - i + 1

                if len_str < min_str:
                    min_str = len_str

                if len_str > max_str:
                    max_str  = len_str

        print(min_str, max_str)