ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

nums = list(map(int, input().split()))

if nums == ascending:
    print("ascending")
elif nums == descending:
    print("descending")
else:
    print("mixed")

ascending2 = True
descending2 = True

for i in range(1,8):
    if nums[i] > nums[i -1]:
        descending2 = False
    elif nums[i] < nums[i -1]:
        ascending2 = False

if ascending2:
    print("ascending")
elif descending2:
    print("descending")
else:
    print("mixed")