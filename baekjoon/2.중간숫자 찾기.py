# 선택테스트 - 중간 숫자 찾기

def find_mid(numbers):
    temp = sorted(numbers)
    target = temp[1]

    return numbers.index(target)
        
numbers = [1,6,4]

print(find_mid(numbers))

