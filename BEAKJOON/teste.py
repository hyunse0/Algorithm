for tc in range(int(input())):
    ans = []
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(n-1):
        for j in range(i+1, n):
            temp = nums[i] * nums[j]
            temp_str = str(temp)
            for k in range(len(temp_str) - 1):
                if temp_str[k] > temp_str[k+1]:
                    break
            else:
                ans.append(temp)
    print('#{} {}'.format(tc+1, max(ans)))