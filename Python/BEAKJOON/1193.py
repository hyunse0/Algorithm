# 백준 1193 분수찾기

# 1번을 꼭짓점으로 하는 삼각형이라고 생각했을 때
#   1
#  2 3
# 4 5 6

# 몇 번째 줄에 위치하는 지 : n(n+1)/2

target = int(input())

x = 1
while target > x*(x+1)/2:
    x += 1

# x번째 줄의 끝, 시작 숫자
e = x*(x+1)/2
s = e - x + 1

# target은 x번째 줄에서 몇 번째 숫자? -> target - s + 1

# x가 홀수라면
# x번째 줄의 분수들 -> x/1, x-1/2, x-2/3, ..., 1/x
if x%2:
    son = int(x - target + s)
    mom = int(x + 1 - son)
# x가 짝수라면
# x번째 줄의 분수들 -> 1/x, 2/x-1, 3/x-2, ..., x/1
else:
    son = int(target - s + 1)
    mom = int(x + 1 - son)

print(str(son) + '/' + str(mom))