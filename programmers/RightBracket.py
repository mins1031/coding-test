from collections import deque
def solution(s):
    answer = True
    left = deque()

    for i in s:
        if s[0] == ')':
            answer = False
            break
        if i == "(":
            left.append(i)
        else:
            if not left:
                continue
            left.popleft()
    if left:
        answer = False
    return answer

s1 = "()()"
s2 = "(())()"
s3 = ")()("
s4 = "(()("
print(solution(s4))