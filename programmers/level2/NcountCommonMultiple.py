def solution(arr):
    answer = 0
    bigger = max(arr)
    count = 1
    while True:
        if answer != 0 :
            break
        standard = bigger * count
        for i in arr:
            if standard % i != 0:
                break
        else:
            answer = standard
        count += 1
    return answer

arr = [2,6,8,14]
arr2 = [1,2,3]

print(solution(arr2))