# import itertools
# def solution(numbers):
#     answer = set()
#     numbers = list(numbers)
#     per = []
#     for i in range(1, len(numbers) + 1):
#         tmp = list(itertools.permutations(numbers, i))
#         per.extend(tmp)
#     tmp_array = []
#     for i in per:
#         tmp_array.append("".join(i))
#
#     for i in tmp_array:
#         i = int(i)
#         if i == 1 or i == 0:
#             continue
#         for j in range(2, int(i)):
#             if i % j == 0:
#                 break
#         else:
#             answer.add(i)
#
#     return len(answer)
#
# numbers = "17"
# numbers2 = "011"
#
# print(solution(numbers))

# 0으로 시작하는 숫자.
# 모든 숫자의 조합.

def isPrimeNumber(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True

def getAllCombination(numbers, numList, leftCipher):
    '''
    numbers : 총 숫자카드 list
    numList : 가능한 숫자 배열 list
    leftCipher : 남은 자릿수
    '''

    # 현재 가능한 숫자 배열 list를 기준으로 추가가 가능한 숫자들은 찾는다.
    newNumList = [[]]
    for li in numList:
        for i in numbers:
            if i in li and li.count(i) <= numbers.count(i) - 1:
                tmp = li[:]
                tmp.append(i)
                newNumList.append(tmp)
            if i not in li:
                tmp = li[:]
                tmp.append(i)
                newNumList.append(tmp)

    leftCipher -= 1

    if leftCipher == 0:
        return newNumList
    else:
        return getAllCombination(numbers, newNumList, leftCipher)

def removeFirstZero(numList):
    for i, num in enumerate(numList):
        firstNumIsZero = bool()

        while True:
            if len(num) >= 2 and num[0] == '0':
                firstNumIsZero = True
            else:
                numList[i] = num
                break

            num = num[1:]

def getUnique2DList(numList):
    for i, val in enumerate(numList):
        tmp = str()
        for char in val:
            tmp += char
        numList[i] = tmp

    newList = list(set(numList))
    return newList

def solution(numbers):
    availableAnswer = getAllCombination(numbers, [[]], len(numbers))
    del availableAnswer[0]
    removeFirstZero(availableAnswer)
    availableAnswer = getUnique2DList(availableAnswer)

    answer = 0
    for val in availableAnswer:
        if isPrimeNumber(int(val)):
            print(val)
            answer += 1

    return answer

numbers = "17"
numbers2 = "011"

print(solution(numbers))