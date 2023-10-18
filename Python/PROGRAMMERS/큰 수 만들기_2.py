# 프로그래머스 큰 수 만들기
def solution(number, k):
    stack = []

    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    answer = ''.join(stack[:len(number)-k])
    return answer

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('99991', 3))