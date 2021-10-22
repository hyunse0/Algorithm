# 백준 1991 트리 순회
import string


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
tree = {}
node = string.ascii_uppercase
for i in range(N):
    tree[node[i]] = ['', '', ''] # 왼쪽자식, 오른쪽 자식, 부모

for _ in range(N):
    perents, left, right = input().split()

    if left != '.':
        tree[perents][0] = left
        tree[left][2] = perents
    
    if right != '.':
        tree[perents][1] = right
        tree[right][2] = perents

pre_lst = []
in_lst = []
post_lst = []

preorder('A')
inorder('A')
postorder('A')

print(''.join(pre_lst))
print(''.join(in_lst))
print(''.join(post_lst))