n = int(input())

max_num = 0
max_man = 0

for man_count in range(n):
    nums = list(map(int, input().split()))
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                temp_sum = nums[i] + nums[j] + nums[k]
                temp_num = int(str(temp_sum)[-1])
                if temp_num >= max_num :
                    max_num = temp_num
                    max_man = man_count + 1

print(max_man)
