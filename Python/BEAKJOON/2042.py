# 백준 2042 구간 합 구하기

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr_sum = [0]
for i in range(1, N+1):
    arr_sum.append(arr_sum[i-1]+arr[i-1])

for _ in range(M+K):
    a, b, c = map(int, input().split())

    # 숫자 변경
    if a == 1:
        tmp = c - arr[b-1]
        arr[b-1] = c

        for i in range(b, N+1):
            arr_sum[i] += tmp
    # 구간 합 출력
    else:
        print(arr_sum[c]-arr_sum[b-1])