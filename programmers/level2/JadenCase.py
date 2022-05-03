def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 and s[0].isalpha():
            answer += s[0].upper()
        elif s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer

s1 = "3people unFollowed me"
s2 = "for the last week"
print(solution(s1))
print(solution(s2))
