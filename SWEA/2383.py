# SWEA 2383 점심 식사시간

T = int(input())

for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]