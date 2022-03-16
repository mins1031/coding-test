import sys

recur = int(sys.stdin.readline())
stack = []
for i in range(recur):
    sentance = sys.stdin.readline().strip().split(' ')
    for j in sentance:
        j.replace("\n", "")
    for j in sentance:
        tmp = list(j)
        tmp.reverse()
        print("".join(tmp), end=' ')
    # print()
