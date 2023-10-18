# 프로그래머스 2*n 타일링

def solution(n):
    tile = [1, 2]
    
    for i in range(2, n):
        tile.append((tile[i-1] + tile[i-2])%1000000007)

    return tile[n-1]