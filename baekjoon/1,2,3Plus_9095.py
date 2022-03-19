test_cnt = int(input())

for i in range(test_cnt):
    nums = [1, 2, 4]
    n = int(input())
    for i in range(3, n):
        nums.append(nums[i-1] + nums[i-2] + nums[i-3])
    print(nums[n - 1])
    nums = [1, 2, 4]
