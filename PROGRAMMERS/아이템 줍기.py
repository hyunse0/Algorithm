# 프로그래머스 아이템 줍기

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    border = set()
    inner = set()
    
    for lx, ly, rx, ry in rectangle:
        # 가로
        for x in range(lx, rx+1):
            for y in [ly, ry]:
                if (x, y) not in inner:
                    border.add((x, y))
        
        # 세로
        for y in range(ly, ry+1):
            for x in [lx, rx]:
                if (x, y) not in inner:
                    border.add((x, y))
        
        for x in range(lx+1, rx):
            for y in range(ly+1, ry):
                if (x, y) in border:
                    border.remove((x, y))
                inner.add((x, y))
    
    queue = deque()
    queue.append((characterX, characterY, 0))
    
    border.remove((characterX, characterY))
    
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y, dist = queue.popleft()
        if x == itemX and y == itemY:
            return dist
        
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            
            if (nx, ny) in border:
                border.remove((nx, ny))
                queue.append((nx, ny, dist+1))


rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
print(solution(rectangle, 1, 3, 7, 8))