import sys
read = sys.stdin.readline

n, k = map(int, read().split())
dy = [0] * (k+1)

for i in range(n):
    w, v = map(int, read().split())
    for j in range(w, k+1):
        dy[j] = max(dy[j], dy[j-w] + v)

print(max(dy))

N, K = map(int, read().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])