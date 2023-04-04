import sys

sys.stdin = open("in_out/chapter1/in1.txt", "rt")

n = int(input())

for i in range(n):
    target_str = list(input())
    reversed_target_str = target_str[::-1]
    target_leng = len(target_str)

    result_str = "YES"
    for i in range(target_leng):
        if str(target_str[i]).lower() != str(reversed_target_str[i]).lower():
            result_str = "NO"

    print(result_str)