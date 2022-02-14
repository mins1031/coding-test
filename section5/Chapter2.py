import sys

sys.stdin = open("in_out/chapter2/in5.txt", "rt")

parent = list(map(str, input()))
stack = list()
count = 0

for i in range(len(parent)):
    if parent[i] == "(":
        if parent[i+1] == ")":
            count += len(stack)
            continue
        stack.append("(")
    else:
        if parent[i-1] == "(":
            continue
        stack.pop()
        count += 1

print(count)

