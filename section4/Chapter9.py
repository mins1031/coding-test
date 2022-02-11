import sys
from collections import deque

sys.stdin = open("in_out/chapter9/in3.txt", "rt")

n = int(input())
inputs = list(map(int, input().split()))

inputs = deque(inputs)
res = list()
standard = 0
inc_val = 0

while True:
    if standard == 0:
        if inputs[0] > inputs[-1]:
            standard = inputs[0]
        else:
            standard = inputs[-1]
        inc_val = abs(inputs.popleft() - inputs.pop())
        res.append("L")
        res.append("R")

    if inputs[0] == standard + inc_val:
        standard = inputs.popleft()
        res.append("L")
    elif inputs[-1] == standard + inc_val:
        standard = inputs.pop()
        res.append("R")
    else:
        break

print(len(res))
for i in res:
    print(i, end="")


