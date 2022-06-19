# 선택테스트 - 아이큐 테스트

def iq_test(list):
    check = []
    result = 0

    for i in list:
        check.append(i%2)
  
    if check.count(1) == 1:
        result = check.index(1) + 1
    elif check.count(0) == 1:
        result = check.index(0) + 1

    return result

list = [110,200,40000,500000,9,00000]

print(iq_test(list))


