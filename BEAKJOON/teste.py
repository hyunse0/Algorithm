arr = [[1, 2, 3], [1, 1, 6], [1, 1, 1]]


def cnt(a, b):
    return a.count(b)

print(list(map(cnt(1), arr, 1)))
# print(sum(map(cnt, arr)))