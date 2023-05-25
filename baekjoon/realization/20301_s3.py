# n, k, m = map(int, input().split())
# k = k - 1
# list = [i for i in range(1, n + 1)]
#
# result = []
# remove_count = 0
# current_index = k
# minus_turn = False
#
# while len(list) != 0:
#     remove_target = list[current_index]
#     list.remove(remove_target)
#     result.append(remove_target)
#
#     remove_count += 1
#     if remove_count == 4 and minus_turn is False:
#         remove_count = 0
#         minus_turn = True
#     elif remove_count == 4 and minus_turn is True:
#         remove_count = 0
#         minus_turn = False
#
#     if minus_turn is False:
#         if (current_index + k) >= len(list):
#             current_index = (current_index + k) - len(list)
#         else:
#             current_index += k
#     else:
#         if (current_index - k) < 0:
#             current_index = len(list) - (current_index - k)
#         else:
#             current_index -= k
#
# for i in result:
#     print(i)

from collections import deque

N, K, M = map(int, input().split())
queue = deque(range(1, N+1))
i = 0
while queue:
    if i//M % 2 == 0:
        for _ in range(K-1):
            queue.append(queue.popleft())
    else:
        for _ in range(K):
            queue.appendleft(queue.pop())
    i += 1
    print(queue.popleft())