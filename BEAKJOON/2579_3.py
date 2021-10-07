# 백준 2579 계단 오르기

N = int(input())
score = [0 for _ in range(301)]
max_score = [0 for _ in range(301)]

for i in range(N):
    score[i+1] = int(input())

max_score[1] = score[1]
max_score[2] = score[1]+score[2]
max_score[3] = max(score[2]+score[3], score[1]+score[3]) # 한 칸 이동, 두 칸 이동

for i in range(4, N+1):
    max_score[i] = max(max_score[i-3]+score[i-1]+score[i], max_score[i-2]+score[i]) # 한 칸 이동, 두 칸 이동

print(max_score[N])