import sys

sys.stdin = open("in_out/chapter7/in5.txt", "rt")

m = int(input())
boxs = list(map(int, input().split()))
clean_count = int(input())

for i in range(clean_count):
    larg_index = boxs.index(max(boxs))
    smal_index = boxs.index(min(boxs))

    boxs[larg_index] -= 1
    boxs[smal_index] += 1

result_large = max(boxs)
result_small = min(boxs)
print(result_large - result_small)




