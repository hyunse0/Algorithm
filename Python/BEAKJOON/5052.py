# 백준 5052 전화번호 목록

def is_same(num1, num2):
    n = min(len(num1), len(num2))

    for i in range(n):
        if num1[i] != num2[i]:
            return True

    return False


def can_cailling():
    for i in range(N):
        for j in range(i+1, N):
            flag = is_same(numbers[i], numbers[j])

            if not flag:
                return 'NO'

    return 'YES'


for _ in range(int(input())):
    N = int(input())
    numbers = [input() for _ in range(N)]

    numbers.sort()

    print(can_cailling())