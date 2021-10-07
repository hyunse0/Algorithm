# 백준 2579 계단 오르기

N = int(input())
score = [0] + [int(input()) for _ in range(N)]

# [현재까지 최고 점수, 한 칸 이동한 횟수]
max_score = [[0, 0] for _ in range(N+1)]
# 0번째 칸은 실제로 밟는 것이 아니므로 횟수를 -1로 초기화
max_score[0][1] = -1

for i in range(N+1):
    if i+1 <= N and max_score[i][1] != 1:
        # 원래 점수
        before1 = max_score[i+1][0]
        # 한 칸 이동
        after1 = max_score[i][0]+score[i+1]

        if before1 < after1:
            max_score[i+1][0] = after1
            max_score[i+1][1] = max_score[i][1] + 1

    if i+2 <= N:
        # 원래 점수
        before2 = max_score[i+2][0]
        # 두 칸 이동
        after2 = max_score[i][0]+score[i+2]

        if before2 < after2:
            max_score[i+2][0] = after2
            max_score[i+2][1] = 0

print(max_score[N][0])