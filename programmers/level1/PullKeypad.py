def solution(numbers, hand):
    answer = ''
    left_nums = [1,4,7]
    right_nums = [3,6,9]

    key_point = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2), 10: (3,0), 0: (3,1), 12: (3,2)}
    left_point = key_point.get(10)
    right_point = key_point.get(12)

    for i in range(len(numbers)):
        num_point = key_point.get(numbers[i])
        if numbers[i] in left_nums:
            answer += "L"
            left_point = num_point
            continue
        elif numbers[i] in right_nums:
            answer += "R"
            right_point = num_point
            continue
        else:
            left_dist = abs(left_point[0] - num_point[0]) + abs(left_point[1] - num_point[1])
            right_dist = abs(right_point[0] - num_point[0]) + abs(right_point[1] - num_point[1])
            if left_dist < right_dist:
                answer += "L"
                left_point = num_point
            elif left_dist > right_dist:
                answer += "R"
                right_point = num_point
            else:
                if hand == "left":
                    answer += "L"
                    left_point = num_point
                else:
                    answer += "R"
                    right_point = num_point

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand2 = "left"
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand3 = "right"

print(solution(numbers, hand))
print(solution(numbers2, hand2))
print(solution(numbers3, hand3))
