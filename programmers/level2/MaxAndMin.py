def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    bigger = max(arr)
    smaller = min(arr)
    answer += str(smaller)
    answer += " "
    answer += str(bigger)

    return answer

def solution2(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    answer += " "

    return str(min(arr)) + " " + str(max(arr))

s1 = "1 2 3 4"
s2 = "-1 -2 -3 -4"
s3 = "-1 -1"

print(solution2(s1))
print(solution2(s2))
print(solution2(s3))