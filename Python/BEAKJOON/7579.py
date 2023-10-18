# 백준 7579 앱

N, M = map(int, input().split())
byte = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

knapsack = [[0 for _ in range(sum(cost)+1)] for _ in range(N+1)]
result = sum(cost)

for c in range(sum(cost)+1):
    for i in range(N+1):
        if c < cost[i]:
            knapsack[i][c] = knapsack[i-1][c]
        else:
            # 비활성화할 경우, 안할 경우
            knapsack[i][c] = max(byte[i] + knapsack[i-1][c-cost[i]], knapsack[i-1][c])
        
        if M <= knapsack[i][c]:
            result = min(result, c)

print(result)

# print('***')
# for k in knapsack:
#     print(k)