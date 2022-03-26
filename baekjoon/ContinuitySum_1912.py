import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
dy = [0] * n
dy[0] = array[0]

for i in range(1, n):
    dy[i] = max(array[i], dy[i-1] + array[i])

print(max(dy))
'''
'''