# 백준 2579 계단 오르기

def up_higher(now, score, cnt):
    # cnt : 연속으로 1칸 오른 횟수
    global max_score

    if now == N:
        max_score = max(max_score, score)
        return
    
    if now+1 <= N and cnt != 1:
        # 한 칸 오르는 경우
        up_higher(now+1, score+scores[now+1], cnt+1)

    # 두 칸 오르는 경우
    if now+2 <= N:
        up_higher(now+2, score+scores[now+2], 0)


N = int(input())
scores = [0] + [int(input()) for _ in range(N)]

max_score = 0
up_higher(0, 0, -1)

print(max_score)