import sys

n = int(sys.stdin.readline().rstrip())

array = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    array.append((x, y))

array = sorted(array, key=lambda x : (x[1], x[0]))

stand = 0
res = 0
for i in range(n):
    if array[i][0] < stand:
        continue
    else:
        if array[i][0] == array[i][1]:
            res += 1
            stand = array[i][1]
            continue
        stand = array[i][1]
        res += 1

print(res)

# for i in range(n-1):
#     present_sub = array[i][1] - array[i][0]
#     next_sub = array[i + 1][1] - array[i + 1][0]
#     if i == n-1:
#         if array[i][0] >= stand:
#             res += 1
#             break
#     if stand > array[i][0] and stand != 0:
#         continue
#     else:
#         if array[i][0] == array[i][1]:
#             res += 1
#             stand = array[i][1]
#             continue
#         if present_sub <= next_sub :
#             stand = array[i][1]
#         else:
#             stand = array[i+1][1]
#         res += 1

