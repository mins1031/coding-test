# 필수 테스트2 - 사용하지 않는 가장 작은 숫자 찾기

def find_smallest(ids):
    ids.sort()
    ids = set(ids)
    ids = list(ids)

    answer = 0
    for i in range(len(ids)):
        if ids[i] != i:
            answer = i
            break

        if i == len(ids) - 1:
            answer = i + 1

    return answer


ids = [0, 1, 2, 3, 9, 7, 5, 4]
print(find_smallest(ids))

ids2 = [0, 1, 2, 4]
print(find_smallest(ids2))

ids3 = [0, 1, 2, 3, 4, 5, 6]
print(find_smallest(ids3))

ids4 = [1, 2, 3, 4, 5, 6]
print(find_smallest(ids4))

