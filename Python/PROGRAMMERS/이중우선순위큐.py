# 프로그래머스 이중우선순위큐

def solution(operations):
    queue = []
    for operation in operations:
        oper = operation.split()
        
        if oper[0] == 'I':
            queue.append(int(oper[1]))
        elif queue and oper[1] == '1':
            queue.pop(queue.index(max(queue)))
        elif queue:
            queue.pop(queue.index(min(queue)))
            
    answer = [0, 0]
    if queue:
        answer = [max(queue), min(queue)]
        
    return answer