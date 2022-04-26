def solution(s):
    answer = ''
    leng = len(s)
    if leng % 2 == 0:
        answer += s[(leng//2) -1]
        answer += s[(leng//2)]
    else:
        answer = s[leng//2]
    return answer

s = "abcde"
s2 = "abcdef"
print(solution(s))
print(solution(s2))