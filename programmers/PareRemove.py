
def solution(s):
    length = len(s)
    stack = [s[0]]

    for i in range(1, length):
        if len(stack) == 0 and i < length:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        answer = 1
    else:
        answer = 0
    return answer


string = "cdcd"
string2 = "baabaa"

print(solution(string2))

# 정확도는 대충 맞는거 같은데 틀린 케이스들은 모두 시간초과. 즉 효율성에서 통과하지 못하는 풀이
# while True:
#     if count == length or len(tmp) == 0:
#         break
#     if tmp[count] == tmp[count-1]:
#         tmp = tmp[0:count - 1] + tmp[count + 1:]
#         count = 1
#         length = len(tmp)
#         print(tmp)
#     else:
#         count += 1
