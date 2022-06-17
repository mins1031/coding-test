from collections import deque

# def solution(n, v):
#     q = deque(v)
#     total_gap = [0] * (n + 1)
#
#     left_total = 0
#     for i in range(n + 1):
#         right = v[i:]
#         temp_total = left_total - sum(right)
#         total_gap[i] = abs(temp_total)
#
#     total_gap[-1] = sum(v)
#
#     return total_gap.index(min(total_gap))

#     minimum_value = min(total_gap)
#
#     for i in range(n + 1):
#         if total_gap[i] == minimum_value:
#             answer = i
#             break
#
#     return answer

def solution(n, v):
    answer = 0
    total_gap = [0] * (n + 1)

    total_left = 0
    total_right = sum(v)
    for i in range(n+1):
        if i == 0:
            total_gap[i] = abs(total_right - total_left)
            continue
        total_left += v[i-1]
        total_right -= v[i-1]

        temp_total = total_left - total_right
        total_gap[i] = abs(temp_total)

    minimum_value = min(total_gap)

    for i in range(n + 1):
        if total_gap[i] == minimum_value:
            answer = i
            break

    return answer

n1 = 5
v1 = [1, 2, 1, 2, 1]
print(solution(n1, v1))

n2 = 7
v2 = [3, 2, 3, 4, -1, -2, -3]
print(solution(n2, v2))



# def solution(n, v):
#     q = deque(v)
#     total_gap = [0] * (n + 1)
#
#     left_total = 0
#     for i in range(n):
#         temp_total = left_total - sum(q)
#         total_gap[i] = abs(temp_total)
#         left_total += q.popleft()
#
#     total_gap[-1] = sum(v)
#
#     return total_gap.index(min(total_gap))

# def solution(n, v):
#     answer = 0
#     total_gap = [0] * (n + 1)
#
#     for i in range(n + 1):
#         left = v[:i]
#         right = v[i:]
#         temp_total = sum(left) - sum(right)
#         total_gap[i] = abs(temp_total)
#
#     minimum_value = min(total_gap)
#
#     for i in range(n + 1):
#         if total_gap[i] == minimum_value:
#             answer = i
#             break
#
#     return answer