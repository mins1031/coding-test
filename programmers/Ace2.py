from itertools import combinations

def combi(array, n):
    result = []
    if n> len(array):
        return result

    if n == 1:
        for i in array:
            result.append(i)
    elif n > 1:
        for i in range(len(array) - n + 1):
            for j in combi(array[i + 1:], n - 1):
                result

def solution(s):
    combi_list = []
    for i in range(1, len(s) + 1):
        combi_list.extend(list(map(''.join, combinations(s, i))))

    combi_list.sort()

    return combi_list[-1]

def solution(s):
    stack = []
    for arg in s:
        while stack and stack[-1] < arg:
            stack.pop()
        stack.append(arg)

    return ''.join(stack)

# s = 'baba'
# print(solution(s))
#
# s2 = 'abcdef'
# print(solution(s2))

s1 = 'bba'
s2 = 'bb'

if s1 < s2:
    print("비교가능")
else:
    print("비교 불가능")


# for i in range(1,5):
#     s.extend(list(map(''.join, combinations('baba', i))))
#
# print(s)
