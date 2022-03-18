n = int(input())
nums = list(map(int, input().split()))
res = 0
wrong = 0
for i in nums:
    if i == 1:
        continue
    for j in range(2, i):
        if (i % j) == 0:
            wrong = 1
            break
    if wrong == 0:
        res += 1
    else:
        wrong = 0
print(res)