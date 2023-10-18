# 백준 1339 단어수학
from collections import defaultdict

N = int(input())

words = []
max_len = 0

for _ in range(N):
    temp = input()
    
    words.append(temp)
    max_len = max(max_len, len(temp))

# 각 자리수에 계산될 알파벳
calculate = [[] for _ in range(max_len)]

for word in words:
    start = max_len - len(word)
    for i in range(start, max_len):
        calculate[i].append(word[i-start])

# print(calculate)

match = {}
number = 9
for j in range(max_len):
    # 해당 자리에 속한 알파벳 중 매칭이 안된 알파벳
    no_match = []
    for alpha in calculate[j]:
        if alpha not in match.keys():
            no_match.append(alpha)

    # 한 개일 경우
    if len(no_match) == 1:
        match[no_match[0]] = number
        number -= 1
    
    # 여러 개일 경우
    else:
        # 해당 자리보다 뒷 자리에 해당 알파벳이 또 쓰이는 경우에 숫자가 커야 한다!
        cnt = defaultdict(int)
        for alpha in no_match:
            for k in range(j+1, max_len):
                if alpha in calculate[k]:
                    cnt[alpha] += calculate[k].count(alpha)
        
        cnt = sorted(cnt, key=lambda x : -cnt[x])
        
        for alpha in cnt:
            match[alpha] = number
            number -= 1

# print(match)

answer = 0
for l in range(max_len):
    total = 0
    for alpha in calculate[l]:
        total += match[alpha]
    
    answer += total * 10**(max_len-1-l)

print(answer)

'''
10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
-> 이 경우 틀림!!
'''