def solution(arr1, arr2):
    answer = []
    leng_arr1 = len(arr1)
    leng_arr2 = len(arr2)
    for col in arr1:
        tmp = [0 for _ in range(leng_arr2)]
        for row in arr2:
            for i in range(len(row)):
                print(tmp)
                tmp[i] += col * row[i]

        answer.append(tmp)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
sub_arr1 = [[3, 3], [3, 3]]
arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
sub_arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, sub_arr1))