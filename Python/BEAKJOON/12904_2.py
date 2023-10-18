# 백준 12904 A와 B

S = list(map(str, input()))
T = list(map(str, input()))

while len(T) > len(S):
    temp = T.pop()
    if temp == 'B':
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)