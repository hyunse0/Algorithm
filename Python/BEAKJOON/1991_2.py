# 백준 1991 트리 순회
from collections import defaultdict


def preorder(node):
    global pre_lst

    if node:
        pre_lst.append(node)
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    global in_lst

    if node:
        inorder(tree[node][0])
        in_lst.append(node)
        inorder(tree[node][1])


def postorder(node):
    global post_lst

    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        post_lst.append(node)


N = int(input())
tree = defaultdict(list)

for _ in range(N):
    perents, left, right = input().split()

    if left != '.':
        tree[perents].append(left)
    else:
        tree[perents].append('')
    
    if right != '.':
        tree[perents].append(right)
    else:
        tree[perents].append('')

pre_lst = []
in_lst = []
post_lst = []

preorder('A')
inorder('A')
postorder('A')

print(''.join(pre_lst))
print(''.join(in_lst))
print(''.join(post_lst))