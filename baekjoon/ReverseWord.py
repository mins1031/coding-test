import sys
from collections import deque

tmp = []
sete = []
left = sys.stdin.readline().rstrip()
res = deque()
ch = 0

for i in range(len(left)):
    if left[i] == '<':
        ch = 1
        tmp.reverse()
        res.extend(tmp)
        tmp = []
    if left[i] == '>':
        ch = 0
        sete.append(left[i])
        res.extend(sete)
        sete = []
        continue

    if ch == 0:
        if left[i] == " ":
            tmp.reverse()
            res.extend(tmp)
            res.append(left[i])
            tmp = []
            continue
        elif i == len(left) -1:
            tmp.append(left[i])
            tmp.reverse()
            res.extend(tmp)
            break
        tmp.append(left[i])
    else:
        sete.append(left[i])

print("".join(res))
