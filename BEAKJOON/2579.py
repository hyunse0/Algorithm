# 백준 2579 계단 오르기

N = int(input())

score = [0]
for _ in range(N):
    score.append(int(input()))

# 두 칸 이동하는 경우 인덱스 에러가 나지 않도록 뒤에 2개의 인덱스를 더 생성
# 인덱스의 숫자를 맞추기 위하여 앞에 1개의 인덱스를 더 생성
arr = [0 for _ in range(N+3)]

for i in range(N, -1, -1):
    # 마지막 칸은 무조건 밟아야 함
    if i == N:
        arr[i] = score[i]
    
    # 한 칸 이동하는 경우 : 그 전 이동은 무조건 2칸 이동이여야 함
    arr[i-1] = max(arr[i-1], arr[i+2] + score[i] + score[i-1])

    # 두 칸 이동하는 경우 : 그 전 이동이 어떤 경우이든 상관없음! 무조건 최대값에 점수 더해주기
    arr[i-2] = max(arr[i-2], arr[i] + score[i-2])

print(arr[1])