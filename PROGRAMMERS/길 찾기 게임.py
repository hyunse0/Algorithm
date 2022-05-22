# 프로그래머스 길 찾기 게임

from collections import deque

def solution(nodeinfo):

    def pre_travers(n):
        nonlocal pre_result

        pre_result.append(n)

        if tree[n][1]:
            pre_travers(tree[n][1])
        
        if tree[n][2]:
            pre_travers(tree[n][2])


    def post_travers(n):
        nonlocal post_result

        post_result.append(n)

        parent = tree[n][0]
        r_child = tree[parent][2]

        if r_child:
            post_travers(r_child)
        
        if parent:
            post_travers(parent)


    nodeinfo = [(i+1, x[0], x[1]) for i, x in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[2], x[1]))
    
    before = deque([nodeinfo[0]])
    # 부모 노드, 자식들
    tree = [[0, 0, 0] for _ in range(len(nodeinfo)+1)]
    
    for node, x, y in nodeinfo[1:]:
        if tree[before[0][0]][2] or y == before[0][2]:
            before.popleft()

        parent = before[0][0]
        tree[node][0] = parent

        # 왼쪽 노드
        if not tree[parent][1] and x < before[0][1]:
            tree[parent][1] = node
        # 오른쪽 노드
        else:
            tree[parent][2] = node

        before.append((node, x, y))
    
    pre_result = []
    pre_travers(nodeinfo[0][0])


    post_result = []
    nodeinfo.sort(key=lambda x: x[1])
    post_travers(nodeinfo[0][0])

    return [pre_result, post_result]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))