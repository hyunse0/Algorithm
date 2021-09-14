# 백준 9935 문자열 폭발

from collections import deque
import sys

def bomb_str(input_string):
    N = len(input_string)
    string = deque()
    for s in input_string:
        string.append(s)

    cnt = 0
    while cnt < N:
        if string[0] == bomb[0]:
            for i in range(len(bomb)):
                if string[i] != bomb[i]:
                    for _ in range(i):
                        string.append(string.popleft())
                        cnt += 1
                    break
            else:
                for _ in range(len(bomb)):
                    string.popleft()
                    cnt += 1
        else:
            string.append(string.popleft())
            cnt += 1
    
    result = ''
    for s in string:
        result += s

    return result


input_string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

while bomb in input_string:
    input_string = bomb_str(input_string)

if not input_string:
    input_string = 'FRULA'

print(input_string)