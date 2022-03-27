import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))
dy = [0] * (n+1)
dy[-1] = nums[-1]

for i in range(n-1, 0, -1):
    tmp_sum = 0
    tmp_max = nums[i-1]

    for j in range(i-1, n):
        if tmp_max < nums[j]:
            tmp_sum += nums[j]
            tmp_max = nums[j]

    dy[i] = tmp_sum + nums[i-1]
    print(dy[i])

print(max(dy))


