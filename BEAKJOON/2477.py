# 백준 2477 참외밭

K = int(input())

lengths = []

max_even = max_odd = even_idx = odd_idx = -1

# 어차피 가로-세로-가로-세로-... 순으로 정렬되어있기 때문에 가로, 세로를 구분할 필요x
for i in range(6):
    way, length = map(int, input().split())

    if not i%2 and max_even < length:
        max_even = length
        even_idx = i
    elif i%2 and max_odd < length:
        max_odd = length
        odd_idx = i
    
    lengths.append(length)

# '홀수 번째 중 가장 큰 변'과 양 옆으로 맞닿아있는 변들의 차 = 짝수 번째 중 작은 사각형의 길이
sub_even = abs(lengths[odd_idx-1] - lengths[(odd_idx+1)%6])
sub_odd = abs(lengths[even_idx-1] - lengths[(even_idx+1)%6])

width = (max_even * max_odd) - (sub_even * sub_odd)
print(K * width)