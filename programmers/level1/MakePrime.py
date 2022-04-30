from itertools import combinations
def solution(nums):
    answer = 0
    madeNums = list(combinations(nums, 3))

    for i in madeNums:
        sum_nums = i[0] + i[1] + i[2]
        for j in range(2, sum_nums):
             if sum_nums % j == 0:
                 break
        else:
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]
print(solution(nums))
