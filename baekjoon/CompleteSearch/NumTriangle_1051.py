import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nums = []

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    tmp_list = []
    for j in range(m):
        tmp_list.append(int(tmp[j]))
    nums.append(tmp_list)

max_side = max(n, m)
res = 1
for k in range(1, max_side):
    for i in range(n):
        for j in range(m):
            if i+k < n and j + k < m:
                if nums[i][j] == nums[i+k][j] == nums[i][j+k] == nums[i+k][j+k]:
                    res = (k+1) * (k+1)
print(res)

