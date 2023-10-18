N = int(input())

idx = list(map(int, input().split()))

answer = []
for i in range(N):
    answer.insert(idx[i], i+1)

answer = answer[::-1]

print(*answer)