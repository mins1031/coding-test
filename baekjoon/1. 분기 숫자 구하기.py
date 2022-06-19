#분기 숫자 구하기

import math

def distinction_quarter(month) :
    if month > 12:
        return "1~12까지의 숫자만 확인할 수 있습니다."
    else:
        quarter = math.ceil(month / 3.0)
        return quarter


month = int(input("분기를 파악할 달을 1~12사이 수로 입력해주세요 : "))
print(distinction_quarter(month))

