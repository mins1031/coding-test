import sys
import re

n = sys.stdin.readline().rstrip()
numbers = re.findall(r'\d+', n)
caler = []

for i in n:
    if i == "+" or i == "-":
        caler.append(i)

res = int(numbers[0])
num_leng = len(numbers)
cal_leng = len(caler)
cnt = 1
if num_leng <= 2:
    if num_leng == 1:
        pass
    else:
        if caler[0] == "-":
            res -= int(numbers[-1])
        else:
            res += int(numbers[-1])
else:
    while True:
        if cnt == num_leng:
            break
        if cnt == num_leng - 1:
            if caler[cnt-1] == "-":
                res -= int(numbers[cnt])
            else:
                res += int(numbers[cnt])
            break
        else:
            if caler[cnt-1] == "-":
                tmp = int(numbers[cnt])
                tmp_c = 1
                for i in range(cnt, cal_leng):
                    if caler[i] == "+":
                        tmp += int(numbers[i+1])
                        tmp_c += 1
                    else:
                        break
                res -= tmp
                cnt += tmp_c
            else:
                res += int(numbers[cnt])
                cnt += 1

print(res)

# 0-100+50-100+50-100 : -400
# 55-50+40 다른 사람 코드 볼것.