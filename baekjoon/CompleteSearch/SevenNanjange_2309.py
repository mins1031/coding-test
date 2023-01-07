
result_sum = 100
nums = []
nanjange_count = 9

for i in range(nanjange_count):
    nums.append(int(input()))

sum_heights = sum(nums)

for i in range(nanjange_count - 2):
    for j in range(i+1, nanjange_count):
        temp_sum = nums[i] + nums[j]
        if sum_heights - temp_sum == result_sum:
            x1 = nums[i]
            y1 = nums[j]

nums.remove(x1)
nums.remove(y1)
nums.sort()

for i in nums:
    print(i)

'''
1. 난장이 리스트를 2중포문을 돌아주는것이다ㅣ
2. 첫 포문은 기준 값을 잡고
3. 둘째 포문은 기준값 다음값부터 값을 잡아가면서
4. 첫 포문, 둘째 포문이 잡은 값을 입력받은 난쟁이 값에서 다 뺌
5. 여기서 100을 찾음
'''