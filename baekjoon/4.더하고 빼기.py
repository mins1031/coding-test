#필수 테스트 - 더하고 빼기

def digit_sub(num):
    count = 0
    value = 0
    apple = [9,18,27,36,45,54,63,72,81,90,99]
    lol = 0;
    while True:
        if count == 0 :
            value = num
            count += 1

        target = list(map(int, str(value)))
        value = value - sum(target)
        lol += 1
        if value < 100:
            if value % 9 == 0:
                return "apple"


num = 170
print(digit_sub(num))

num = 170
print(digit_sub(num))

