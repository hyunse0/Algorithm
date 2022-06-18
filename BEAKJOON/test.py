from math import ceil

A, B, V = map(int, input().split())

# 하루에 올라갈 수 있는 높이 : A-B
print(ceil((V-A)/(A-B))+1)