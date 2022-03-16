import sys

n = int(sys.stdin.readline())
stack = []
vps = []
no_break = 0
for i in range(n):
    vps.append(sys.stdin.readline())

for i in vps:
    stack = []
    no_break = 0
    for j in i:
        if j == "(":
            stack.append("(")
        if j == ")":
            if not stack:
                no_break = 1
                break
            stack.pop()
    if not stack and no_break == 0:
        print("YES")
    else:
        print("NO")
