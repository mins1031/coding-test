import sys

rod = sys.stdin.readline().rstrip()

stack = []
rod_cnt = 0
for i in range(len(rod)):
    if i == len(rod) - 1:
        if rod[i] == '(':
            continue
    if rod[i] == '(':
        if rod[i+1] == ')':
            rod_cnt += len(stack)
            continue
        rod_cnt += 1
        stack.append(rod[i])
    else:
        if rod[i-1] == "(":
            continue
        elif len(stack) == 0:
            continue
        stack.pop()
print(rod_cnt)