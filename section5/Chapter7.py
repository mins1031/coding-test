from collections import deque
import sys

sys.stdin = open("in_out/chapter7/in5.txt", "rt")

n = input()
test_case = int(input())
for _ in range(test_case):
    explain = input()
    temp = []
    no = False
    for i in n:
        if i not in explain:
            no = True
            break
        temp.append(explain.index(i))

    if no:
        print("NO")
        continue

    for i in range(1, len(temp)):
        if temp[i] < temp[i -1]:
            print("NO")
            break
    else:
        print("YES")


