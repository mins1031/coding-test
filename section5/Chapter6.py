from collections import deque
import sys

sys.stdin = open("in_out/chapter6/in5.txt", "rt")

n, m = map(int, input().split())
patients = list(map(int, input().split()))

patients = deque([(i, idx) for idx, i in enumerate(patients)])
res = 0
while patients:
    if patients[0] == max(patients, key=lambda x: x[0]):
        res += 1
        if patients[0][1] == m:
            break
        patients.popleft()
    else:
        patients.append(patients.popleft())

print(res)
