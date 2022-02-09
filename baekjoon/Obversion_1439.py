binaries = input()
# binaries_list = list(map(int, binaries))
#
# zero_dup_count = 0
# zero_count = 0
# for binary in binaries_list:
#     if binary == 0:
#         if zero_dup_count == 0:
#             zero_count += 1
#             zero_dup_count += 1
#     else:
#         if zero_dup_count > 0:
#             zero_dup_count = 0
#
# one_dup_count = 0
# one_count = 0
#
# for binary in binaries_list:
#     if binary == 1:
#         if one_dup_count == 0:
#             one_count += 1
#             one_dup_count += 1
#     else:
#         if one_dup_count > 0:
#             one_dup_count = 0
#
# if one_count >= zero_count:
#     print(zero_count)
# else:
#     print(one_count)

# ===================더 나은 코드====================

count0 = 0
count1 = 0

if binaries[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(binaries) - 1):
    if binaries[i] != binaries[i + 1]:
        if binaries[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))