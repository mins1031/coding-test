
def solution(s):
    answer = -1
    tmp = s
    count = 1

    while count >= len(s):
        if s[count] == s[count-1]:
            if count == 1:
                tmp = tmp[count+1:]
            else:
                tmp = tmp[0:count-1] + tmp[count+1:]
                count = 0
                print(tmp)


    if not tmp:
        answer = 1
    else:
        answer = 0
    return answer


# string = str(input())
string = "cdcd"
string2 = "baabaa"

print(string2[0:1] + string2[3:])
print(solution(string2))

