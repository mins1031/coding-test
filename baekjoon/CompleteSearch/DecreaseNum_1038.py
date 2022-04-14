import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
# 풀이 아이디어 감탄;;;
nums = []
for i in range(1, 11):
    for com in combinations(range(0, 10), i):
        com = list(com)
        com.sort(reverse=True)
        nums.append(int("".join(map(str, com))))

nums.sort()

try:
    print(nums[n])
except:
    print(-1)

# cnt = 10
# i = 11
# res = 0
# while True:
#     print(i)
#     print(cnt)
#     if len(str(n)) == 1:
#         print(n)
#         break
#
#     tmp = list(map(int, str(i)))
#     for j in range(1, len(tmp)):
#         if tmp[j-1] <= tmp[j]:
#             break
#         elif tmp[j-1] > tmp[j] and j == len(tmp) -1:
#             cnt += 1
#     i += 1
#     if cnt == n:
#         res = i
#         print(res)
#         break
# else:
#     print("-1")

# for i in range(1, 11):
#     for com in combinations(range(0, 10), i):
#         print(list(com))