import sys

sys.stdin = open("in_out/chapter1/in1.txt", "rt")

n = int(input())
line = [0] * (n+1)
line[1] = 1
line[2] = 2
for i in range(3, n+1):
    line[i] = line[i-2] + line[i-1]

print(line[n])