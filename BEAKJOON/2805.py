import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

H = max(trees)
my_tree = 0
stop = True

while stop:
    for tree in trees:
        if tree > H:
            my_tree += 1

            if my_tree >= M:
                print(H)
                stop = False
    
    H -= 1