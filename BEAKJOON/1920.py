import sys

def isin(A, B):
    A.sort()

    result = [0]*M

    for i in range(M):
        start = 0
        end = N-1

        while start <= end:
            center = (start + end)//2
            
            if B[i] < A[center]:
                end = center-1
            elif B[i] > A[center]:
                start = center+1
            else:
                result[i] += 1
                break
    
    return result


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

result = isin(A, B)

for num in result:
    print(num)