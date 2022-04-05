n = int(input())
point = []


def back(p):
    sta = 0
    # for i in range(p+1):


for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

point.sort()
big = max(point)[0] + 1
target = max(point)[1]
small = min(point)[0]
height = 0

for x, y in point:
    if y > height:
        height = y

house = [[0 for _ in range(big)] for _ in range(height)]

print(point)
print(target)
bigger = 0
biggery = 0
total = 0
for i in range(small, target+1):
    # if point[]
    if point[i][0] > bigger:
        bigger = point[i][0]
        biggery = point[i][1]
        total += point[i][1]
    else:
        total += biggery
# for x, y in point:
#     if x == target:
#         total += y
#         break
#     else:
#         if x > biggerx:
#             biggerx = x
#             biggery = y
#             total += y
#         else:
#             total += biggery
bigger = 0
biggery = 0
for i in range(n-1, target, -1):
    if point[i][0] > bigger:
        bigger = point[i][0]
        biggery = point[i][1]
        total += point[i][1]
    else:
        total += biggery

print(total)