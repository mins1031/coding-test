import sys

sys.stdin = open("in_out/chapter8/in1.txt", "rt")


n = int(input())
words = dict()
for i in range(n):
    value = input()
    words[value] = 1

for i in range(n-1):
    used = input()
    words[used] = 0

print(words.items())
for key, val in words.items():
    if val == 1:
        print(key)

