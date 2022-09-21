arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_sum = [[0 for _ in range(4)] for _ in range(4)]

for i in range(1, 4):
    for j in range(1, 4):
        arr_sum[i][j] = arr[i-1][j-1] + arr_sum[i-1][j] + arr_sum[i][j-1] - arr_sum[i-1][j-1]

print(arr_sum)