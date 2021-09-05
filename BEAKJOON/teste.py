fish = [(0, 2), (0, 1), (3, 1), (2, 1)]

fish.sort(key=lambda x: (x[0], x[1]))

print(fish[0])


# 거리가 1인 애들을 구해보자
# distance1 = deque()
# for dx, dy in dxy:
#     nx, ny = x+dx, y+dy
#     distance1.append((nx, ny))

# 거리가 2인 애들을 구해보자
# distance2 = deque()
# while distance1:
#     x, y = distance1.popleft()
#     for dx, dy in dxy:
#         nx, ny = x+nx, y+ny
#         distance2.append((nx, ny))

