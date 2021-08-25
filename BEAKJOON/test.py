def KMP(pattern, text):
    M = len(pattern)
    N = len(text)

    # 문자열 매칭 실패 시 돌아갈 곳을 저장
    fail = [0]*M
    i = 0
    j = 1
    while j < M:
        # 첫 번째는 -1 저장
        fail[0] = -1

        # 만약 똑같은 문자가 있다면, 앞 쪽 문자의 인덱스 저장
        if pattern[i] == pattern[j]:
            fail[j] = i
            i += 1
            j += 1
        # 아니라면 한 칸 옮기기
        else:
            j += 1
    
    print(fail)

    # 문자열 매칭
    i = j = 0
    while True:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = j - fail[j]




pattern = 'ABCDABD'
# [-1, 0, 0, 0, 0, 1, 2]
text = 'ABCABCDABABCDABCDABDE'
KMP(pattern, text)
