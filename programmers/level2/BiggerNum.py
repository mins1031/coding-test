from collections import deque
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    # for i in numbers:
    #     if not stack:
    #         stack.append(i)
    #         continue
    #     stack.append(i)
    #     for j in range(len(stack)-1, 0, -1):
    #         if stack[j][0] > stack[j-1][0]:
    #             stack[j-1], stack[j] = stack[j], stack[j-1]
    #             continue
    #         elif stack[j][0] < stack[j-1][0]:
    #             continue
    #         elif stack[j][0] == stack[j-1][0]:
    #             if len(stack[j]) == 1 and len(stack[j-1]) == 1:
    #                 continue
    #             elif len(stack[j]) == 1 and len(stack[j-1]) == 2:
    #                 if stack[j-1][0] > stack[j-1][1]:
    #                     stack[j - 1], stack[j] = stack[j], stack[j - 1]
    #                 continue
    #             elif len(stack[j]) == 2 and len(stack[j-1]) == 1:
    #                 if stack[j][0] < stack[j][1]:
    #                     stack[j - 1], stack[j] = stack[j], stack[j - 1]
    #                 continue
    #             elif len(stack[j]) == 2 and len(stack[j-1]) == 2:
    #                 if stack[j][1] > stack[j-1][1]:
    #                     stack[j - 1], stack[j] = stack[j], stack[j - 1]
    #                 continue

    return "".join(stack)


numbers = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers2))

# array = list(map(int, array))
# tmp = []
# for i in array:
#     tmp.append(int("".join(i)))
