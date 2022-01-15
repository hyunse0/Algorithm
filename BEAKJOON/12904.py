# 백준 12904 A와 B

def game(string):
    global answer
    
    if len(string) == len(T):
        if string == T:
            answer = 1
        return
    
    game(string + 'A')
    game(string[::-1] + 'B')


S = input()
T = input()

answer = 0
game(S)

print(answer)