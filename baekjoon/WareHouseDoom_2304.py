n = int(input())
point = []

def back(p):

    sta = 0
    # for i in range(p+1):


for i in range(n):
    x, y = map(int, input().split())

    point.append((x, y))

point.sort()
big = max(point)[0]

house = [[0 for _ in range(big+1)] for _ in range(big+1)]


