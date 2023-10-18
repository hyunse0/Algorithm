# 백준 11725 트리의 부모 찾기
N = int(input())

parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())

    # j가 루트 노드거나, 부모 노드가 이미 존재한다면 -> parent
    if j == 1 or parent[j]:
        parent[i] = j
    else:
        parent[j] = i

for node in parent[2:]:
    print(node)